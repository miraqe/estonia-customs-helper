# Customs Declaration Helper

An unofficial helper for people and small companies in Estonia who receive parcels from outside the EU and declare them themselves in e-MTA.

It does three things:

1. Picks the form: nothing to file, the private postal declaration, or the full import declaration (H1).
2. Estimates customs duty and VAT from the commodity code, price, shipping and exchange rate.
3. Lists what to enter in each field of the e-MTA import declaration, with the reason for each value.

It files nothing and sends nothing anywhere. Everything you type stays in your browser and is gone when you close or reload the page.

## Use it

**Open the helper: [Customs Declaration Helper](https://miraqe.github.io/estonia-customs-helper/)**

You can also download `index.html` and open it in a browser. There is nothing to install.

The page is in English and Estonian ([Tollideklaratsiooni abiline](https://miraqe.github.io/estonia-customs-helper/et.html)), with a link between the two at the top.

## Limits

- Not made or endorsed by the Estonian Tax and Customs Board (EMTA). The person who files a declaration is responsible for every value in it.
- Duty rates are EU third-country rates at 6-digit level, checked on 29 September 2026. Rates can differ between 10-digit codes under one heading. Confirm in the Estonian customs tariff (ETT).
- Anti-dumping duties are flagged, not calculated.
- Storage permit details are built in for FedEx only, taken from a declaration filed in June 2026. For other carriers, use your arrival notice.
- The private postal declaration is recommended where it applies, but its fields are not mapped yet.
- Road, rail and sea transport deductions by distance are not calculated.

## Updating the duty table

The rates are embedded in `index.html`. To refresh them, download `data/eu_duty_by_origin.csv` from
https://github.com/checkdutyrates/us-tariff-data and run:

    python3 build/make_duty.py eu_duty_by_origin.csv index.html

Then update the "checked on" date in the page footer and in this file.

## Updating the Estonian page

`index.html` is the source. `et.html` is built from it:

    python3 build/make_et.py index.html et.html

The script stops and names the string if any English text it expects has changed, so new or edited text needs its Estonian pair added in `build/make_et.py`.

## Where the duty rates come from

The rates are the EU's own customs tariff rates, the same ones Estonia applies. This project does not read them from the EU directly. It uses a public copy:

- The UK government publishes the EU tariff through its Trade Tariff service, in the part marked "XI" (Northern Ireland, where the EU tariff applies).
- The open collection `checkdutyrates/us-tariff-data` on GitHub packages that publication as a table. Despite its name, the collection also holds EU data.
- This project takes the EU table from that collection and embeds the standard third-country rate for each 6-digit heading.

The official sources are the EU's TARIC database and the Estonian customs tariff (ETT). Always confirm a rate there before filing.

## Data credit

Contains public sector information licensed under the Open Government Licence v3.0 (UK Trade Tariff, XI service), via the checkdutyrates/us-tariff-data collection. The licence requires this credit.
