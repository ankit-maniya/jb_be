-- =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =
-- loatwise_price_details
-- =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =
select extract(
		day
		from l2.l_entrydate
	) as day,
	extract(
		month
		from l2.l_entrydate
	) as month,
	extract(
		year
		from l2.l_entrydate
	) as year,
	sum(l2.l_weight) as weight,
	sum(l2.l_numofdimonds) as totaldimonds,
	round(
		sum(
			case
				when l2.l_multiwithdiamonds = true then l2.l_price * l2.l_numofdimonds
				else l2.l_price * l2.l_weight
			end
		),
		2
	) as totalMoneyDayWise
from public.loats as l2
where l2.userid = 7
	and l2.isactive = true
	and l2.isdelete = false
	and extract(
		year
		from l2.l_entrydate
	) in (
		SELECT extract(
				year
				from l.l_entrydate
			) as years
		FROM public.loats as l
		where l.userid = 7
			and l.isactive = true
			and l.isdelete = false
		group by years
	)
group by l2.l_entrydate
order by year,
	month,
	day -- =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =
	-- 
	-- =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =