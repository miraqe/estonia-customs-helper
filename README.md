# Customs Declaration Helper

An unofficial helper for people and small companies in Estonia who receive parcels from outside the EU and declare them themselves in e-MTA.

It does three things:

1. Picks the form: nothing to file, the private postal declaration, or the full import declaration (H1).
2. Estimates customs duty and VAT from the commodity code, price, shipping and exchange rate.
3. Lists what to enter in each field of the e-MTA import declaration, with the reason for each value.

It files nothing and sends nothing anywhere. Everything you type stays in your browser and is gone when you close or reload the page.

## Use it

Open the published page (see the link in the repository's "About" box), or download `index.html` and open it in a browser. There is nothing to install.

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

## Data credit

Duty rates contain public sector information licensed under the Open Government Licence v3.0, from the UK Trade Tariff (XI) service, via the checkdutyrates/us-tariff-data collection.
