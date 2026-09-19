# September 18, 2026 — Audit corrections and cleanup

Anselm Hook and OpenAI Codex worked together on this pass. Anselm approved the
[source-linked audit](2026-09-18-correctness-audit.md) and asked for a persistent
devlog. This record describes the applied changes, rather than claiming that
every remaining sentence has been independently established.

## Editorial scope

Kept nine chapters, 50 parts, their order, and all part images. Revised prose in
32 parts (see [index](changed-parts.txt)). Kept Mixed Messages and the emotional
sequence preceding Emerging Superpowers. Unverifiable quantities and causal
claims were removed or narrowed. Earlier wording remains in Git history.

## Factual corrections applied

| Parts | Disposition |
|---|---|
| 01.01 | ATS-3 described as an early whole-Earth color image; Gaia credits Lovelock and Margulis and describes feedback, not biodiversity maximization. |
| 02.02–03 | Distinguished alarming media messages from established mechanisms; removed the unverified Hawking quote and Thiel/Mars association. |
| 03.02–05 | Consecutive civic-app numbering and proper names; Louisiana MRGO distinguished from Katrina flood-defense failures; polio progress, CFC phaseout, and pre-Paris pledges described accurately. |
| 04.02–03 | Malthus distinguished from later ecological models; acidification explained as CO2 uptake with falling pH; global 1998 bleaching estimate corrected. Removed unsupported emissions quantities, universal coral-extinction deadline, beetle/mortgage causal chain and coastal-majority claim. |
| 04.04–05 | Fisheries collapse distinguished from extinction; fertilizer and insecticide effects separated; pollinator claims narrowed; DDT food chain corrected; unsourced plastic tonnage removed; aquifer compaction qualified. Ausubel’s land-sparing argument attributed and linked without a universal recovery claim. |
| 05.02–04 | Ward’s warming/anoxia/hydrogen-sulfide mechanism separated from methane; chronology shortened and eras, dinosaurs, mammals and etymology corrected. Removed unsupported biodiversity, recovery-time and land-use quantities. Anthropocene remains informal in the 2015 framing. |
| 06.03–06 | June 2015 G7 declaration distinguished from a treaty; Haiti generalization narrowed; isolated consumer gestures distinguished from collective action; dark future labeled a feared scenario; risks to other species retained. |
| 07.01–07 | Models compare scenarios, not all possible paths or certain futures. Clarified public access, calibration versus testing, uncertain structure/inputs/outputs, and community choice of values. Replaced opaque labels with concealed costs and information asymmetry. |
| 08.01–04 | Lansing and Kremer coauthorship and full paper title; removed unsourced policy-impact inference. Verified Jensi Sartin’s Bali fish-bank story. Yellowstone account allows multiple drivers. Gopalpura/Alwar water restoration paraphrased with attribution instead of long quotation and exact village counts. |
| 08.05–08 | Removed disputed spill quantities/health extrapolations and inferred private BP models; Grand Coulee salmon barrier retained, unsupported grizzly conclusion removed. Lake Merritt’s restricted flow and 2013 works corrected. Nestlé proposal distinguished from approval; Indian fishing image explicitly identified as an illustration. |
| 08.09 | Removed unreliable drought notebook statistics (temperature percentage, per-well rate, crop/job/ranking/snowpack/groundwater-age/subsidence claims) rather than guess corrections. Replaced with a four-row table from NASA 2014 and contemporary CDFA/PPIC reporting, naming denominators, period, and scope. Drought remains a meaningful concept; reservoir storage is distinguished from all available water. |
| 08.10 | Delta smelt distinguished from longfin smelt; annual lifecycle clarified; unsourced fish count, jobs, elevation and supply-share quantities removed. |

Mechanical corrections in `copy-edits.json` remain applied. The misleading NASA
headline was removed in favor of the HANDY paper already listed. The 2040 headline
now identifies reporting on a modeled risk, not a government prediction. The fire
was on Bellandur Lake, Bangalore. Digital Democracy’s URL was repaired. Antifragile
and Intertwingled moved from people to Books with verified authors and years.

## Additional verification sources

The audit snapshot contains the main sources. Additional checks used:

- [USACE MRGO history](https://www.mvn.usace.army.mil/Missions/Environmental/MRGO-Ecosystem-Restoration/History-of-MRGO/).
- [June 2015 G7 declaration](https://g7.utoronto.ca/summit/2015elmau/2015-G7-declaration-en.html).
- [The Moth: Jensi Sartin, The Fish Bank](https://www.themoth.org/stories/the-fish-bank), recorded November 11, 2014.
- [Alameda County: Oakland Estuary watershed](https://acfloodcontrol.org/resources/explore-watersheds/oakland-estuary-watershed/) for Lake Merritt’s 2013 works.
- [Northwest Power and Conservation Council: Grand Coulee impacts on fish](https://www.nwcouncil.org/reports/columbia-river-history/grandcouleeimpactsonfish/).
- [EcoTippingPoints: Rajasthan restoration](https://www.ecotippingpoints.org/our-stories/indepth/india-rajasthan-rainwater-harvest-restoration-groundwater-johad.html).
- [NASA’s December 2014 water estimates](https://www.nasa.gov/news-release/nasa-analysis-11-trillion-gallons-to-replenish-california-drought-losses/).
- [CDFA’s August 2014 account of PPIC water-use denominators](https://plantingseedsblog.cdfa.ca.gov/index.php/2014/08/06/water-california-analysis-public-policy-institute-california/).
- [Bellandur Lake reporting, June 19, 2015](https://www.latimes.com/world/asia/la-fg-fire-springs-forth-on-india-lake-20150619-story.html).

## Reading list and attribution

Added links and brief descriptions for 17 Voices. Safa Motesharrei and Jorge Rivas
link to the coauthored HANDY research; no unrelated namesake profile was substituted.
Other entries link to institutional/author profiles or Wikipedia. Four dated,
reusable portraits (Kalnay, Ackerman, Darwin, Wilson) are stored locally, with
source, photographer, date and license in `source/resources.json`; full attribution
is available under Portrait credits. No guessed or generated likenesses were used.

Added covers for Antifragile, Intertwingled, and the author-requested *The Origin
and Nature of Life on Earth*. The latter is explicitly dated 2016: this is an
approved exception to the period bibliography, not evidence for redating the essay.
[Cambridge’s publication record](https://assets.cambridge.org/97810096/33772/frontmatter/9781009633772_frontmatter.pdf)
confirms Eric Smith, Harold J. Morowitz, and first publication in 2016.

Removed the repeated cover byline and sidebar author link; kept search attribution
and a footer author link to a brief About page, with Substack, Medium, and X links. README now records this joint
cleanup. The separate contemporary draft was not modified.

## Verification and limits

Validation passed: the generator renders 50 parts; all nine chapter names and the 50-part image sequence match the preceding revision; 32 parts have prose changes. Local assets and fragment targets resolve, IDs are unique, and JSON-LD parses without an unverified datePublished. Desktop Voices and 390px mobile About/Voices layouts were checked in the browser; the water table scrolls inside its container without page overflow. New covers were visually checked. Git diff whitespace checks passed. June 24, 2015 remains
an inferred reference-entry date; no datePublished is asserted. Current sources
used for fact checking are not silently added as 2015 readings. Historical external
links can still fail or redirect; a complete external-link and inherited-image
rights audit remains separate work. Scientific models remain illustrative and
contestable; removing unsupported claims is not evidence that they were all false.
