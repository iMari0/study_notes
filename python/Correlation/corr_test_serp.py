import numpy as np
import sqlalchemy as sa
import pandas as pd

DATABASE = "prd"
USER = "iuliano"
PASSWORD = "7xmajmuWCWj0c2N74TRz"
HOST = "10.217.198.5"
PORT = "5439"
SCHEMA = "public"

engine = sa.create_engine('postgres://iuliano:7xmajmuWCWj0c2N74TRz@10.217.198.5:5439/prd')
connection = engine.connect()

# Creating connection and assigning SQL query results into 'df'
with engine.connect() as conn, conn.begin():
    df = pd.read_sql("""
select distinct kdb.company_id,
                kdb.order_head_eff_vf,
                kdb.order_head_eff_vt,
                decode(kdb.min_order_id_1, null, 0, 1)                 as follow_up,
                case
                    when to_date(kdb.order_head_eff_vf_1, 'YYYY-MM') <=
                         to_date(dateadd(month, 6, kdb.order_head_eff_vt), 'YYYY-MM') then 1
                    else 0 end                                         as follow_up_time,
                decode(kdb.sales_promo_kru_1, 'KRU', 1, 0)             as kru,
                Sum(decode(customer_report.company_id, NULL, 0, pageviews)) as customer_report_views
from migration.kru_data_base kdb
         join reporting.v_customer_contract_history cch
              on kdb.min_order_id = cch.order_id
         left join (
    SELECT fgp.date,
           fgp.companyid     as company_id,
           fgp.customerid    as customer_id,
           sum(fgp.sessions) as pageviews
    FROM reporting.fact_gbq_pageviews fgp
             left join reporting.dim_virtual_page_title dvpt
                       on dvpt.virtual_page_title_sk = fgp.virtual_page_title_sk
             join reporting.dim_trafficsource dt
                  on dt.trafficsource_sk = fgp.trafficsource_sk
             join reporting.dim_wlw_user_roles ur
                  on fgp.wlw_user_roles_sk = ur.wlw_user_roles_sk
    WHERE 1 = 1
      and fgp.isdachhost = TRUE
      and dvpt.virtual_page_title in ('customer_report')
      and dt.trafficsource = 'external'
      AND fgp."date" >= '2019-01-01'
      and wlw_user_roles in ('supplier', 'buyer,supplier', 'supplier,buyer', 'undefined')
    group by 1, 2, 3
) customer_report
                   on kdb.company_id = customer_report.company_id and
                      customer_report.date between kdb.order_head_eff_vf and kdb.order_head_eff_vt
where 1 = 1
  and kdb.main_order_reason = 'Core Product'
group by 1,2,3,4,5,6
""", conn)