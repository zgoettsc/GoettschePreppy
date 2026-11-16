# usage: rj KEY CODE ID...   CODE: PJA | SI | SEED | WM:<name> | OTHER:<text>
rj() { k=$1; c=$2; shift 2; for id in "$@"; do
  case $c in
    PJA) r="copyright notice in the frame (Patrick J. Alexander) although the PLANTS record says Copyright=false";;
    SI) r="copyright notice in the frame (Smithsonian Institution) although the PLANTS record says Copyright=false";;
    SEED) r="seed photograph only; not useful for identification in the field";;
    WM:*) r="copyright notice in the frame (${c#WM:}) although the PLANTS record says Copyright=false";;
    OTHER:*) r="${c#OTHER:}";;
  esac; printf "%s\t%s\t%s\n" "$k" "$id" "$r" >> /home/user/goettschepreppy/scripts/plants/rejected.tsv; done; }
