-- =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =
-- daywise_loats_price_details
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
	day;
-- =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =
-- 
-- =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =
select l1.id,
	l1.l_weight,
	l1.partyid,
	l1.l_cuttingtype,
	l1.l_entrydate,
	l1.isactive,
	round(
		sum(
			case
				when l1.l_multiwithdiamonds = true then l1.l_price * l1.l_numofdimonds
				else l1.l_price * l1.l_weight
			end
		),
		2
	) as totalMoneyDayWise,
	sum(l1.l_weight)
from public.loats l1
group by l1.l_cuttingtype,
	l1.partyid,
	l1.l_entrydate,
	l1.id
having l1.partyid = 5
	and l1.isactive = true
	and l1.isdelete != false
order by l1.partyid,
	l1.l_entrydate;
-- ======================================================================
--		all_partywise_yearwise_loats
-- Select Loat with price Loat_price whcih can return partywise loat details
-- Require l_year & partyid for this filter
-- =====================================================================
select l1.id,
	sum(l1.l_weight) as total_weight,
	p1.p_name,
	l1.l_cuttingtype,
	l1.l_entrydate,
	l1.l_year,
	l1.l_month,
	l1.old_partyid,
	l1.l_price,
	round(
		sum(
			case
				when l1.l_multiwithdiamonds = true then l1.l_price * l1.l_numofdimonds
				else l1.l_price * l1.l_weight
			end
		),
		2
	) Amount
from public.loats l1,
	public.partys p1
group by l1.l_cuttingtype,
	l1.l_entrydate,
	l1.id,
	l1.l_month,
	l1.l_year,
	p1.p_name,
	p1.id,
	l1.old_partyid,
	l1.l_weight
having l1.partyid = p1.id
	and l1.l_year = 2022
	and l1.partyid = 11
order by l1.l_cuttingtype,
	l1.l_entrydate,
	l1.l_month;
-- ======================================================================
--		day_wise_total
-- Select Grand Total which can return below fileds
-- Require l_year, l_month for this filter
--Total weight, datewise, month, year, amount, num_of_dimonds
--1585.66, "2021-04-01", 4, 2021, 29860.19, 21165	
-- =====================================================================
select sum(l1.l_weight) as total_weight,
	l1.l_entrydate,
	l1.l_month,
	round(
		sum(
			case
				when l1.l_multiwithdiamonds = true then l1.l_price * l1.l_numofdimonds
				else l1.l_price * l1.l_weight
			end
		),
		2
	) Amount,
	sum(l1.l_numofdimonds) as l_numofdimonds,
	l1.l_year
from public.loats l1
group by l1.l_entrydate,
	l1.l_month,
	l1.l_year,
	l1.isdelete
having l1.l_year = 2022
	and l1.l_month = 5
	and l1.l_partyid = 11
	and l1.isdelete = false
order by l1.l_entrydate;
-- ======================================================================
--	month_wise_total
-- Select Grand Total which can return below fileds
-- Require l_year for this filter
--Total weight, month, year, amount, num_of_dimonds
--1585.66, 4, 2021, 29860.19, 21165	
-- =====================================================================
select l1.l_month,
	l1.l_year,
	sum(l1.l_weight) as total_weight,
	sum(l1.l_numofdimonds) as l_numofdimonds,
	round(
		sum(
			case
				when l1.l_multiwithdiamonds = true then l1.l_price * l1.l_numofdimonds
				else l1.l_price * l1.l_weight
			end
		),
		2
	) Amount
from public.loats l1
group by l1.l_month,
	l1.l_year,
	l1.isdelete
having l1.l_year = 2021
	and l1.isdelete = false
order by l1.l_month desc;
-- ======================================================================
--	year_wise_total
-- Select Grand Total which can return below fileds
-- Nothing Require for this filter
--Total weight, year, amount, num_of_dimonds
--1585.66, 2021, 29860.19, 21165	
-- =====================================================================
select l1.l_year,
	sum(l1.l_weight) as total_weight,
	sum(l1.l_numofdimonds) as l_numofdimonds,
	round(
		sum(
			case
				when l1.l_multiwithdiamonds = true then l1.l_price * l1.l_numofdimonds
				else l1.l_price * l1.l_weight
			end
		),
		2
	) Amount
from public.loats l1
group by l1.l_year,
	l1.isdelete
having l1.isdelete = false
order by l1.l_year desc;
-- ======================================================================
--	get_all_party_data_based_on_month_year
-- Select Grand Total which can return below fileds
-- Require l_year, userid, l_month for this filter, It is JOIN Query
-- TotalAmount,
-- TotalWeight,
-- TotalDimonds,
-- DimondWiseTotalAmount,
-- DimondWiseTotalWeight,
-- DimondWiseTotalWeight WeightWiseTotalAmount,
-- WeightWiseTotalWeight,
-- WeightWiseTotalDimonds;
-- =====================================================================
select l1.partyid,
	p1.p_name,
	l1.l_year,
	l1.l_month,
	l1.l_cuttingtype,
	round(
		sum(
			case
				when l1.l_multiwithdiamonds = true then l1.l_price * l1.l_numofdimonds
				else l1.l_price * l1.l_weight
			end
		),
		2
	) TotalAmount,
	sum(l1.l_weight) as TotalWeight,
	sum(l1.l_numofdimonds) as TotalDimonds,
	round(
		sum(
			case
				when l1.l_multiwithdiamonds = true then l1.l_price * l1.l_numofdimonds
				else 0
			end
		),
		2
	) DimondWiseTotalAmount,
	round(
		sum(
			case
				when l1.l_multiwithdiamonds = true then l1.l_weight
				else 0
			end
		),
		2
	) DimondWiseTotalWeight,
	sum(
		case
			when l1.l_multiwithdiamonds = true then l1.l_numofdimonds
			else 0
		end
	) DimondWiseTotalDimonds,
	round(
		sum(
			case
				when l1.l_multiwithdiamonds = false then l1.l_price * l1.l_weight
				else 0
			end
		),
		2
	) WeightWiseTotalAmount,
	round(
		sum(
			case
				when l1.l_multiwithdiamonds = false then l1.l_weight
				else 0
			end
		),
		2
	) WeightWiseTotalWeight,
	sum(
		case
			when l1.l_multiwithdiamonds = false then l1.l_numofdimonds
			else 0
		end
	) WeightWiseTotalDimonds
from public.loats l1,
	public.partys p1
group by l1.l_year,
	l1.isdelete,
	l1.l_cuttingtype,
	l1.partyid,
	l1.userid,
	l1.l_month,
	p1.p_name,
	p1.id
having l1.isdelete = false
	and l1.l_year = 2022
	and l1.partyid = p1.id
	and l1.userid = 7
	and l1.partyid = 11
order by p1.p_name asc;