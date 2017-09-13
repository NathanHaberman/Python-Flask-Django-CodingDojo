#1
-- select sum(amount) as 'march_2012_revenue'
-- from billing
-- where month(charged_datetime) = 3 and year(charged_datetime) = 2012

#2
-- select sum(amount) as 'client_2_revenue'
-- from billing
-- where client_id = 2

#3
-- select client_id, domain_name
-- from sites
-- where client_id = 10

#4
-- select year(created_datetime) as 'year', month(created_datetime) as 'month', count(domain_name) as 'domains_created'
-- from sites
-- where client_id = 1
-- group by year(created_datetime), month(created_datetime)

#5
-- select sites.domain_name as 'domain_name', count(leads.leads_id) as 'number_of_leads', sites.created_datetime as 'created_at'
-- from sites
-- join leads on leads.site_id = sites.site_id
-- where year(sites.created_datetime) = 2011 and month(sites.created_datetime) <= 2 and day(sites.created_datetime) <= 15
-- group by sites.domain_name

#6
-- select clients.first_name, clients.last_name, count(leads.leads_id) as 'leads_count'
-- from clients
-- join sites on clients.client_id = sites.client_id
-- join leads on sites.site_id = leads.leads_id
-- where year(leads.registered_datetime) = 2011
-- group by clients.client_id

#7
-- select clients.first_name, clients.last_name, month(leads.registered_datetime) as 'month', count(leads.leads_id) as 'leads_count_per_month'
-- from clients
-- join sites on clients.client_id = sites.client_id
-- join leads on sites.site_id = leads.leads_id
-- where year(leads.registered_datetime) = 2011 and month(leads.registered_datetime) <= 6
-- group by clients.client_id

#8
-- select clients.client_id, clients.first_name, clients.last_name, sites.domain_name,  count(leads.leads_id) as 'number_of_leads'
-- from clients
-- join sites on sites.client_id = clients.client_id
-- join leads on sites.site_id = leads.site_id
-- where year(leads.registered_datetime) = 2011
-- group by sites.domain_name
-- order by client_id asc

#9
-- select clients.client_id, clients.first_name, clients.last_name, sum(billing.amount) as 'revenue', month(billing.charged_datetime) as 'month', year(billing.charged_datetime) as 'year'
-- from clients
-- join billing on billing.client_id = clients.client_id
-- group by month(billing.charged_datetime)
-- order by clients.client_id asc

#10
-- select clients.first_name, clients.last_name, group_concat(sites.domain_name)
-- from clients
-- join sites on clients.client_id = sites.client_id
-- group by clients.client_id


