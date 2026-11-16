# Sources

`index.json` is the only file in the kit that holds URLs. Pages cite by `key`. The renderer prints
title, publisher and date; the fetcher uses `url` for Large downloads.

- `licence_class`: `public-domain` and `open` ship inside every binder; `restricted` is fetched per
  household for Large downloads only; `blocked` hosts refused automated capture when the household
  binder was built and are attempted again at download.
- `household_cited_by`: pages in the owner's binder that cited this source (provenance).
- `cited_by`: kit pages citing it, filled by the build.
- `additions/<worker>.json`: new sources proposed by content workers, merged by the coordinator.
