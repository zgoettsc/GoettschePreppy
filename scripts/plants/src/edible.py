# Safe-starter wild edibles with low look-alike risk, plus a few foraged plants that have a deadly
# double (risk 'caution' or 'do-not-eat') so the pair can be shown side by side.
#
# risk:  starter    = common, distinctive, no dangerous look-alike when the listed features all match
#        caution    = edible, but has a dangerous look-alike or a preparation rule that must be followed
#        do-not-eat = listed only because people forage it and a deadly plant mimics it; the binder's
#                     rule is never to eat it from the wild
# use: parts eaten and how, with the safety rule for each.

E = []
def e(key, sci, common, risk, id, use, habitat, look=None, src=None, groups=None, **kw):
    E.append(dict(key=key, sci=sci, common=common, group='edible', groups=groups or ['edible'], risk=risk,
                  kind='plant', id=id, use=use, habitat=habitat, look=look or {}, src=src or ['plants', 'ncsu-toolbox'], **kw))

# ---------------------------------------------------------------- lawn and garden weeds
e('dandelion', 'Taraxacum officinale', ['Dandelion'], 'starter',
  ['Leaves only in a ground-level rosette, deeply toothed, hairless.',
   'One yellow flower head per HOLLOW, leafless stalk with milky sap.',
   'Round white puffball seed head.'],
  'Young leaves raw or cooked (bitter later in the season); flowers; roasted roots.',
  'Lawns, roadsides and fields in every state.')
d_plantain_id = ['Rosette of broad oval leaves with 3 to 7 strong parallel veins; pull a leaf and the veins stretch out like strings.',
                 'Long narrow spikes of tiny green-brown flowers.']
e('broadleaf-plantain', 'Plantago major', ['Broadleaf plantain', 'Common plantain'], 'starter',
  d_plantain_id, 'Young leaves raw or cooked; older leaves are stringy, cook them. Crushed leaf used on stings and scrapes.',
  'Lawns, paths and packed ground in every state.')
e('narrowleaf-plantain', 'Plantago lanceolata', ['Narrowleaf plantain', 'Ribwort'], 'starter',
  ['Rosette of long narrow leaves with 3 to 5 parallel ribs.',
   'Short dark cone-shaped flower head on a long grooved stalk, with a ring of white stamens.'],
  'Young leaves cooked; seeds.', 'Lawns, roadsides and fields in every state.')
e('lambs-quarters', 'Chenopodium album', ["Lamb's quarters", 'White goosefoot', 'Pigweed'], 'caution',
  ['Upright weed, 1 to 6 feet.',
   'Diamond- or goose-foot-shaped leaves with wavy teeth.',
   'Young leaves and tips covered with a white mealy powder that wipes off and sheds water.'],
  'Young leaves and tips cooked like spinach. Boil and discard the water: it piles up nitrate and oxalate. Not from heavily manured or drought-stressed ground, and not a staple.',
  'Gardens, fields and disturbed ground in every state.')
e('purslane', 'Portulaca oleracea', ['Purslane'], 'starter',
  ['Low mat with thick, smooth, reddish stems.',
   'Fleshy paddle-shaped leaves; clear watery juice.',
   'Tiny yellow five-petalled flowers.'],
  'Leaves and stems raw or cooked. Contains oxalate: eat as part of a varied diet.',
  'Gardens, sidewalk cracks and bare ground in every state.',
  {'spotted-spurge': 'Break a stem: purslane has clear juice and fleshy leaves; spurge has MILKY sap and thin leaves.'})
e('redroot-amaranth', 'Amaranthus retroflexus', ['Redroot amaranth', 'Redroot pigweed'], 'caution',
  ['Upright weed, 1 to 5 feet, with a pink-red taproot.',
   'Rough hairy stem; oval leaves with prominent veins.',
   'Dense bristly green flower spikes.'],
  'Young leaves cooked; seeds. Like lamb\'s quarters it piles up nitrate and oxalate: boil and discard the water; not from manured ground.',
  'Gardens, fields and feedlots in every state.')
e('stinging-nettle', 'Urtica dioica', ['Stinging nettle'], 'starter',
  ['Plant 2 to 6 feet with a SQUARE stem.',
   'Paired, coarsely toothed, pointed leaves.',
   'Stinging hairs on stem and leaves; drooping strings of tiny green flowers.'],
  'Young tops (before flowering) cooked; cooking or drying removes the sting. Wear gloves to pick.',
  'Moist rich ground, stream banks and farmsteads in nearly every state.')
e('wood-nettle', 'Laportea canadensis', ['Wood nettle'], 'starter',
  ['Plant 2 to 4 feet in moist woods, with stinging hairs.',
   'Leaves ALTERNATE (not paired), broad, oval and toothed.',
   'Branched clusters of tiny greenish flowers.'],
  'Young tops cooked like stinging nettle. Gloves.',
  'Moist woods and floodplains of the East and Midwest.')
e('common-chickweed', 'Stellaria media', ['Common chickweed'], 'starter',
  ['Low sprawling plant of cool seasons.',
   'Small paired oval pointed leaves.',
   'ROUND stem with a single line of hairs that switches sides at each leaf pair.',
   'Tiny white flowers with five petals so deeply split they look like ten.'],
  'Leaves and stems raw or cooked.', 'Gardens, lawns and shady ground in every state.',
  {'scarlet-pimpernel': 'Scarlet pimpernel has square stems, orange flowers and black dots under the leaves.'})
e('yellow-wood-sorrel', 'Oxalis stricta', ['Yellow wood sorrel', 'Sourgrass'], 'starter',
  ['Leaves of three HEART-shaped leaflets (like clover with a notch).',
   'Small five-petalled yellow flowers; seed pods like tiny okra.',
   'Sour lemony taste.'],
  'Leaves, flowers and pods raw as a nibble. High in oxalate: small amounts only.',
  'Lawns, gardens and woods in nearly every state.')
e('curly-dock', 'Rumex crispus', ['Curly dock', 'Yellow dock'], 'caution',
  ['Rosette of long narrow leaves with strongly wavy, crinkled edges.',
   'Tall stalk with dense clusters of small green flowers that turn rusty brown.'],
  'Young leaves cooked, changing the water once. High oxalate: small amounts, not daily.',
  'Fields, roadsides and ditches in every state.')
e('sheep-sorrel', 'Rumex acetosella', ['Sheep sorrel'], 'starter',
  ['Small plant with arrowhead-shaped leaves (two lobes at the base pointing out).',
   'Thin stalks of tiny reddish flowers.',
   'Sour taste.'],
  'Leaves raw as a sour nibble. High oxalate: small amounts.',
  'Acid sandy soils, lawns and fields in every state.')
e('garlic-mustard', 'Alliaria petiolata', ['Garlic mustard'], 'starter',
  ['First year: rosette of kidney-shaped scalloped leaves.',
   'Second year: stalk 1 to 3 feet with triangular toothed leaves and small white four-petalled flowers.',
   'Crushed leaves smell of garlic.'],
  'Leaves and flowering tops raw or cooked; roots like horseradish. Invasive: pick all you like.',
  'Woods and shady edges of the East, Midwest and Northwest.')
e('shepherds-purse', 'Capsella bursa-pastoris', ["Shepherd's purse"], 'starter',
  ['Ground rosette of toothed leaves (like a small dandelion).',
   'Thin stalk with tiny white four-petalled flowers.',
   'Flat HEART-shaped seed pods.'],
  'Young leaves raw or cooked; seed pods.', 'Gardens, lawns and roadsides in every state.')
e('common-blue-violet', 'Viola sororia', ['Common blue violet'], 'starter',
  ['Low plant with heart-shaped scalloped leaves.',
   'Blue-violet (sometimes white) five-petalled flowers on their own stalks.'],
  'Young leaves and flowers raw or cooked. Not the roots or seeds.',
  'Lawns, woods and yards of the East and Midwest.')
e('white-clover', 'Trifolium repens', ['White clover'], 'starter',
  ['Creeping lawn plant; leaves of three round leaflets, often with a pale V mark.',
   'White round flower heads.'],
  'Flowers and young leaves, cooked or dried for tea (raw in quantity is hard to digest).',
  'Lawns and pastures in every state.')
e('red-clover', 'Trifolium pratense', ['Red clover'], 'starter',
  ['Upright clover with leaves of three oval leaflets with a pale V mark.',
   'Pink-purple round flower heads.'],
  'Flowers fresh or dried for tea; young leaves cooked.', 'Fields and roadsides in every state.')
e('chicory', 'Cichorium intybus', ['Chicory'], 'starter',
  ['Ground rosette of toothed leaves like dandelion, but rough-hairy.',
   'Stiff branching stalk 1 to 4 feet.',
   'Sky-blue flowers with square-tipped petals, open in the morning.'],
  'Young leaves cooked; roasted root as a coffee substitute.', 'Roadsides and fields in every state.')
e('common-burdock', 'Arctium minus', ['Common burdock'], 'caution',
  ['First year: very large heart-shaped leaves, woolly beneath, with hollow stalks.',
   'Second year: stalk with purple thistle-like flowers in hooked burs that stick to clothing.'],
  'First-year root, peeled and cooked; young peeled leaf stalks. Dig only plants you saw in bur the year before: rosettes of rhubarb (poisonous leaves) and foxglove are confused with it.',
  'Farmyards, roadsides and waste ground in nearly every state.')
e('henbit', 'Lamium amplexicaule', ['Henbit'], 'starter',
  ['Low plant with SQUARE stems.',
   'Round scalloped leaves that clasp the stem in pairs.',
   'Small pink-purple tube flowers.'],
  'Leaves and stems raw or cooked.', 'Gardens and lawns in early spring, in every state.')
e('purple-deadnettle', 'Lamium purpureum', ['Purple deadnettle'], 'starter',
  ['Low plant with SQUARE stems; upper leaves purple-tinged and crowded.',
   'Triangular hairy scalloped leaves; small pink-purple tube flowers.',
   'No sting.'],
  'Leaves raw or cooked.', 'Gardens, lawns and fields in the East, Midwest and Northwest.')
e('common-mallow', 'Malva neglecta', ['Common mallow', 'Cheeseweed'], 'starter',
  ['Low sprawling plant with round, shallowly lobed leaves on long stalks.',
   'Small white to pale pink five-petalled flowers.',
   'Flat round seed heads like little cheese wheels.'],
  'Leaves and "cheeses" raw or cooked; thickens soup.', 'Gardens, yards and farmyards in nearly every state.')
e('black-mustard', 'Brassica nigra', ['Black mustard', 'Wild mustard'], 'starter',
  ['Plant 2 to 6 feet with lower leaves deeply lobed, upper narrow.',
   'Small bright yellow four-petalled flowers.',
   'Short pods pressed against the stem.'],
  'Young leaves cooked; flower buds; seeds as a spice.', 'Fields and roadsides in most states, abundant in California.')
e('watercress', 'Nasturtium officinale', ['Watercress'], 'caution',
  ['Grows IN cold flowing water or on wet mud.',
   'Leaves of 3 to 9 smooth roundish leaflets, the end one largest.',
   'Small white four-petalled flowers.',
   'Peppery taste.'],
  'Leaves raw or cooked. Water may carry parasites (liver fluke) and farm runoff: cook it unless the water source is known clean.',
  'Springs, streams and ditches in nearly every state.',
  {'cursed-buttercup': 'Cursed buttercup has yellow buttercup flowers and lobed leaves; watercress has white four-petalled flowers and leaflets in rows.'})
e('common-sow-thistle', 'Sonchus oleraceus', ['Common sow thistle'], 'starter',
  ['Upright plant with milky sap and a hollow stem.',
   'Soft, lobed leaves that clasp the stem with pointed ear-like lobes; soft prickles.',
   'Small yellow dandelion-like flowers on branched stalks.'],
  'Young leaves raw or cooked.', 'Gardens, fields and roadsides in every state.')
e('prickly-lettuce', 'Lactuca serriola', ['Prickly lettuce', 'Wild lettuce'], 'starter',
  ['Plant 1 to 6 feet with milky sap.',
   'Leaves twisted upright, clasping the stem, with a row of prickles down the midrib underneath.',
   'Small pale yellow flowers.'],
  'Very young leaves cooked (bitter).', 'Roadsides and waste ground in every state.')
e('fireweed', 'Chamerion angustifolium', ['Fireweed'], 'starter',
  ['Plant 2 to 6 feet, often in big stands after fire or logging.',
   'Narrow willow-like leaves whose veins join in loops before the edge.',
   'Spike of four-petalled magenta flowers; long thin seed pods with fluff.'],
  'Young shoots and leaves cooked; flowers raw.', 'Burns, clearings and roadsides in the North, the West and Alaska.')
e('miners-lettuce', 'Claytonia perfoliata', ["Miner's lettuce"], 'starter',
  ['Small succulent plant of cool, shady spring ground.',
   'Upper leaves fused into a round disc around the stem.',
   'Tiny white flowers rising from the centre of the disc.'],
  'Leaves and stems raw or cooked.', 'Shady woods and slopes of the Pacific states and the interior West.')
e('spring-beauty', 'Claytonia virginica', ['Spring beauty'], 'starter',
  ['Small spring plant with one pair of long grass-like leaves.',
   'White to pink five-petalled flowers striped with darker pink.',
   'Small round tuber underground.'],
  'Leaves raw or cooked; tubers cooked. Take few: it is slow to recover.',
  'Woods and lawns of the East and Midwest.')
e('wild-asparagus', 'Asparagus officinalis', ['Wild asparagus'], 'starter',
  ['Spring spears identical to garden asparagus.',
   'Later: feathery bush 3 to 6 feet with red berries (do not eat the berries).',
   'Last year\'s dry tan stalks mark the spot.'],
  'Young spears raw or cooked. The red berries are poisonous.',
  'Ditches, fence lines and roadsides in nearly every state, most of all the Midwest and West.')
e('ostrich-fern', 'Matteuccia struthiopteris', ['Ostrich fern', 'Fiddlehead fern'], 'caution',
  ['Grows in clumps (crowns) on river floodplains.',
   'Fiddleheads smooth, bright green, with a deep U-shaped groove on the inside of the stalk.',
   'Brown papery scales on the coils; no fuzz.'],
  'Tightly coiled fiddleheads, boiled 15 minutes (raw or lightly cooked fiddleheads have caused food poisoning). Take only half the coils from a crown.',
  'Floodplain woods of the North and upper Midwest.',
  src=['plants', 'umaine-fiddleheads'], look={'bracken-fern': 'Bracken fiddleheads are fuzzy and branch into three; ostrich fern fiddleheads are smooth with a U-shaped groove.'})
e('broadleaf-cattail', 'Typha latifolia', ['Broadleaf cattail', 'Common cattail'], 'caution',
  ['Grows standing in shallow water in large stands.',
   'Long flat leaves, spongy inside, with a rounded base.',
   'The brown sausage-shaped seed head on a stalk: present only in summer and fall.'],
  'Young shoots (peeled), green flower spikes cooked, pollen, and starchy rootstocks. Harvest only from a stand you identified by its brown spikes the summer before: iris grows in the same water and is toxic. The water may be polluted.',
  'Marshes, ditches and pond edges in every state.')
e('narrowleaf-cattail', 'Typha angustifolia', ['Narrowleaf cattail'], 'caution',
  ['Like broadleaf cattail but with narrower leaves.',
   'A gap of bare stem between the upper (male) and lower (brown) parts of the spike.'],
  'Same uses and same rule: harvest only from stands identified by their spikes.',
  'Marshes and ditches in most states.')
e('jerusalem-artichoke', 'Helianthus tuberosus', ['Jerusalem artichoke', 'Sunchoke'], 'starter',
  ['Tall sunflower, 5 to 10 feet, in patches.',
   'Rough sandpapery leaves; yellow sunflower heads 2 to 3 inches across.',
   'Knobby tubers underground.'],
  'Tubers raw or cooked (cause gas). Dig in fall after frost.',
  'Moist fields, roadsides and stream banks of the East, Midwest and Plains.')
e('common-sunflower', 'Helianthus annuus', ['Common sunflower'], 'starter',
  ['Tall coarse plant with rough heart-shaped leaves.',
   'Yellow flower heads with a brown centre.'],
  'Seeds.', 'Fields and roadsides of the Plains and West; nearly every state.')
e('groundnut', 'Apios americana', ['Groundnut', 'Potato bean'], 'starter',
  ['Twining vine (no tendrils) on shrubs near water.',
   'Leaves of 5 to 7 smooth pointed leaflets.',
   'Clusters of maroon-brown and pink pea flowers.',
   'A string of round tubers like beads along the root.'],
  'Tubers, cooked (some people react to raw ones). Seeds cooked.',
  'Moist thickets and stream banks of the East and Midwest.')
e('broadleaf-arrowhead', 'Sagittaria latifolia', ['Broadleaf arrowhead', 'Wapato', 'Duck potato'], 'caution',
  ['Emergent plant in shallow water.',
   'Arrowhead-shaped leaves with veins fanning out from the base.',
   'White three-petalled flowers in whorls of three on a stalk.',
   'Egg-sized tubers at the ends of runners in the mud in fall.'],
  'Tubers, cooked. Water may be polluted.', 'Marshes and pond edges in every state.',
  {'arrow-arum': 'Arrow arum has a green hood-shaped flower and a vein running along the leaf edge; arrowhead has white three-petalled flowers.'})
e('wild-rice', 'Zizania palustris', ['Northern wild rice', 'Manoomin'], 'starter',
  ['Tall grass, 3 to 10 feet, growing in shallow lakes and slow rivers.',
   'Seed heads with upper part bearing long-bristled seeds.'],
  'Grain, parched or cooked. Beware ergot (black hard bodies replacing grains); discard any.',
  'Lakes and rivers of Minnesota, Wisconsin, Michigan and nearby.')
e('glasswort', 'Salicornia depressa', ['Glasswort', 'Sea bean', 'Pickleweed'], 'starter',
  ['Succulent jointed green stems with no visible leaves, like tiny asparagus.',
   'Turns red in fall.'],
  'Young tips raw or cooked; very salty.', 'Salt marshes of the coasts and salty inland flats.')

# ---------------------------------------------------------------- onions and bulbs (caution)
_onion = ('Bulbs and leaves raw or cooked, ONLY if every bulb smells of onion or garlic. Smell EACH '
          'bulb with clean hands: onion smell on your fingers carries to the next bulb. If any bulb in '
          'a clump does not smell of onion, throw the whole clump away. No onion smell means death camas.')
_onion_look = {'meadow-death-camas': 'Death camas has NO onion smell. That is the test, bulb by bulb.',
               'mountain-death-camas': 'Death camas has no onion smell.',
               'foothill-death-camas': 'Death camas has no onion smell.',
               'nuttalls-death-camas': 'Death camas has no onion smell.',
               'star-of-bethlehem': 'Star of Bethlehem has flat leaves with a white midstripe and no onion smell.',
               'daffodil': 'Daffodil bulbs have no onion smell.',
               'fly-poison': 'Fly poison has no onion smell.'}
e('meadow-garlic', 'Allium canadense', ['Meadow garlic', 'Wild onion', 'Canada onion'], 'caution',
  ['Thin flat leaves from a small bulb covered in a fibrous net.',
   'Head of pink-white flowers, often mixed with or replaced by small bulblets.',
   'Strong onion smell from every part.'],
  _onion, 'Prairies, meadows, open woods and roadsides of the East, Midwest and Plains.', _onion_look)
e('field-garlic', 'Allium vineale', ['Field garlic', 'Crow garlic'], 'caution',
  ['HOLLOW round leaves like chives, in lawns.',
   'Head of small bulblets with long tails, sometimes a few flowers.',
   'Strong garlic smell.'],
  _onion, 'Lawns, pastures and fields of the East, Midwest and South.', _onion_look)
e('nodding-onion', 'Allium cernuum', ['Nodding onion'], 'caution',
  ['Flat narrow leaves from a slender bulb.',
   'Pink to white flowers on a stalk that bends over like a shepherd\'s crook.',
   'Onion smell.'],
  _onion, 'Prairies, rocky slopes and open woods across most of the country.', _onion_look)
e('textile-onion', 'Allium textile', ['Textile onion', 'Prairie onion'], 'caution',
  ['Two narrow leaves from a bulb wrapped in a fibrous net coat.',
   'Upright cluster of white star flowers.',
   'Onion smell.'],
  _onion, 'Dry prairies and plains of the Great Plains and Rockies.', _onion_look)
e('ramps', 'Allium tricoccum', ['Ramps', 'Wild leek'], 'caution',
  ['Patches in rich spring woods.',
   'One to three broad, smooth, flat leaves from a bulb; stem base often reddish.',
   'Leaves gone by early summer; then a ball of white flowers on a bare stalk.',
   'Strong onion-garlic smell.'],
  'Leaves raw or cooked; bulbs sparingly (slow-growing). Crush a leaf from EACH plant: no onion-garlic smell means lily of the valley or false hellebore.',
  'Rich moist woods of the Northeast, Appalachians and upper Midwest.',
  {'lily-of-the-valley': 'Lily of the valley has no onion smell and grows in larger mats with bell flowers.',
   'green-false-hellebore': 'False hellebore has PLEATED leaves on a stem and no onion smell.',
   'california-corn-lily': 'Corn lily has pleated leaves and no onion smell.',
   'autumn-crocus': 'Autumn crocus leaves have no onion smell.'})
e('camas', 'Camassia quamash', ['Common camas', 'Blue camas'], 'do-not-eat',
  ['Grass-like leaves from a bulb, in wet spring meadows.',
   'Spike of BLUE star-shaped flowers.'],
  'A traditional staple food, slow-roasted. Listed here because death camas grows in the same meadows and the bulbs are nearly identical out of flower. Do not dig camas for food.',
  'Wet meadows of the Pacific Northwest, northern Rockies and Great Basin.',
  {'meadow-death-camas': 'Edible camas has blue flowers; death camas has cream flowers. Out of flower they cannot be told apart.',
   'mountain-death-camas': 'Camas flowers are blue; death camas flowers are cream.',
   'foothill-death-camas': 'Camas flowers are blue; death camas flowers are cream.'})
e('wild-carrot', 'Daucus carota', ["Wild carrot", "Queen Anne's lace"], 'do-not-eat',
  ['Flat lacy umbrella of white flowers, often with one dark purple floret in the centre.',
   'Flower head curls into a bird\'s-nest shape as it goes to seed.',
   'HAIRY stem; carrot smell from the root.',
   'Stiff three-forked bracts under the flower head.'],
  'The ancestor of the garden carrot. Listed here only because poison hemlock and water hemlock kill people who think they found it. The binder\'s rule: never eat carrot-family plants from the wild.',
  'Fields, roadsides and waste ground in every state.',
  {'poison-hemlock': 'Hemlock stem is smooth and purple-blotched; wild carrot is hairy. Do not rely on this to eat it.',
   'water-hemlock': 'Water hemlock grows in wet ground with a smooth stem; wild carrot on dry ground with a hairy stem. Do not rely on this to eat it.',
   'fools-parsley': 'Fool\'s parsley has drooping bracts and a smooth stem.'})

# ---------------------------------------------------------------- berries and fruit
e('wild-strawberry', 'Fragaria virginiana', ['Wild strawberry', 'Virginia strawberry'], 'starter',
  ['Low plant with leaves of three toothed leaflets.',
   'White five-petalled flowers.',
   'Small red strawberries with seeds in pits on the surface.'],
  'Berries raw; leaves for tea (fresh or fully dried, not wilted).',
  'Fields, prairies, woods edges in nearly every state.')
e('common-blackberry', 'Rubus allegheniensis', ['Common blackberry', 'Allegheny blackberry'], 'starter',
  ['Arching thorny canes 3 to 8 feet.',
   'Leaves of 3 to 5 toothed leaflets.',
   'White flowers; black berries that keep the white core when picked.'],
  'Berries raw or cooked; young peeled shoots; leaves for tea (fresh or fully dried).',
  'Fields, clearings and woods edges of the East and Midwest.')
e('northern-dewberry', 'Rubus flagellaris', ['Northern dewberry'], 'starter',
  ['Trailing prickly canes along the ground.',
   'Leaves of 3 to 5 toothed leaflets; white flowers.',
   'Black berries that keep the core when picked.'],
  'Berries raw or cooked.', 'Fields, roadsides and open woods of the East and Midwest.')
e('black-raspberry', 'Rubus occidentalis', ['Black raspberry', 'Black cap'], 'starter',
  ['Arching canes with a white-blue waxy coating and hooked prickles.',
   'Leaves of 3 to 5 leaflets, white underneath.',
   'Black berries that come off HOLLOW (like a thimble).'],
  'Berries raw or cooked.', 'Woods edges and fence rows of the East, Midwest and Plains.')
e('red-raspberry', 'Rubus idaeus', ['Red raspberry', 'American red raspberry'], 'starter',
  ['Upright bristly canes 2 to 6 feet.',
   'Leaves of 3 to 5 toothed leaflets, whitish beneath.',
   'Red berries that come off hollow.'],
  'Berries raw or cooked; leaves for tea (fresh or fully dried).',
  'Clearings, burns and woods edges across the North, the mountains and Alaska.')
e('thimbleberry', 'Rubus parviflorus', ['Thimbleberry'], 'starter',
  ['Thornless shrub, 3 to 6 feet.',
   'Large soft maple-like leaves.',
   'Large white flowers; soft red flattened berries that come off hollow.'],
  'Berries raw.', 'Woods edges and clearings of the West, Alaska and the upper Great Lakes.')
e('salmonberry', 'Rubus spectabilis', ['Salmonberry'], 'starter',
  ['Prickly shrub, 3 to 12 feet, in moist coastal forest.',
   'Leaves of three toothed leaflets.',
   'Magenta flowers; yellow-orange to red raspberry-like berries.'],
  'Berries raw; young peeled shoots.', 'Moist forests of the Pacific coast and Alaska.')
e('wineberry', 'Rubus phoenicolasius', ['Wineberry'], 'starter',
  ['Arching canes covered in red bristly hairs.',
   'Leaves of three leaflets, white beneath.',
   'Bright red glossy berries in a sticky husk.'],
  'Berries raw. Invasive: pick freely.', 'Woods edges of the Northeast and mid-Atlantic.')
e('red-mulberry', 'Morus rubra', ['Red mulberry'], 'starter',
  ['Tree with large toothed leaves, some mitten-shaped with lobes, rough on top.',
   'Milky sap in leaf stalks.',
   'Blackberry-like fruits that ripen red to dark purple, on a short stem.'],
  'Ripe fruit raw or cooked. Unripe fruit and the milky sap upset the stomach.',
  'Bottomland woods of the East, Midwest and Plains.', groups=['edible', 'firewood'])
e('white-mulberry', 'Morus alba', ['White mulberry'], 'starter',
  ['Tree with glossy toothed leaves, some lobed, smooth on top.',
   'Blackberry-like fruits, white, pink or dark purple when ripe.'],
  'Ripe fruit raw or cooked. Unripe fruit upsets the stomach.',
  'Yards, fence rows and towns in nearly every state.')
e('lowbush-blueberry', 'Vaccinium angustifolium', ['Lowbush blueberry'], 'starter',
  ['Low woody shrub, under 2 feet, in acid sandy or rocky ground.',
   'Small glossy oval leaves, finely toothed.',
   'Blue berries, each with a five-pointed crown at the bottom; many tiny seeds.'],
  'Berries raw or cooked.', 'Barrens, burns and pine woods of the Northeast and upper Midwest.',
  {'eastern-black-nightshade': 'Nightshade is a soft weed with berries on a stalk and a green star-shaped cap; blueberry is a woody shrub with a crown at the bottom of each berry.',
   'deadly-nightshade': 'Belladonna berries sit singly on a soft leafy plant with a green star behind each.'})
e('highbush-blueberry', 'Vaccinium corymbosum', ['Highbush blueberry'], 'starter',
  ['Woody shrub, 5 to 12 feet, in swamps and acid soils.',
   'Oval leaves; white urn-shaped flowers.',
   'Blue berries with a crown at the bottom.'],
  'Berries raw or cooked.', 'Swamps, bogs and acid woods of the East.',
  {'eastern-black-nightshade': 'Nightshade is a soft weed with a green cap on each berry; blueberry is a woody shrub with a crown at the bottom of each berry.'})
e('big-huckleberry', 'Vaccinium membranaceum', ['Thinleaf huckleberry', 'Big huckleberry'], 'starter',
  ['Woody shrub, 2 to 6 feet, in mountain forests and burns.',
   'Thin oval pointed leaves, finely toothed.',
   'Purple-black berries with a crown at the bottom.'],
  'Berries raw or cooked.', 'Mountain forests of the Northwest and northern Rockies.')
e('large-cranberry', 'Vaccinium macrocarpon', ['Large cranberry', 'American cranberry'], 'starter',
  ['Trailing evergreen vine in bogs.',
   'Small leathery oval leaves.',
   'Red berries, sour.'],
  'Berries cooked or raw.', 'Bogs of the Northeast and upper Midwest.')
e('lingonberry', 'Vaccinium vitis-idaea', ['Lingonberry', 'Lowbush cranberry'], 'starter',
  ['Low evergreen shrub, under a foot.',
   'Small glossy leathery leaves with black dots beneath.',
   'Clusters of red berries.'],
  'Berries cooked or raw.', 'Northern forests, bogs and tundra of Alaska, the far North and northern New England.')
e('american-elderberry', 'Sambucus nigra ssp. canadensis', ['American elderberry', 'Elderberry'], 'caution',
  ['WOODY shrub, 5 to 12 feet, with corky bumps on the stems.',
   'Paired leaves of 5 to 11 toothed leaflets.',
   'Large FLAT-topped clusters of tiny white flowers in early summer.',
   'Drooping clusters of tiny dark purple-black berries in late summer.'],
  'Ripe berries COOKED (raw berries, seeds, stems and leaves cause vomiting); flowers cooked or for tea. Strip berries from all stems.',
  'Moist ground, ditches and woods edges of the East, Midwest and Plains; related elders in the West.',
  {'water-hemlock': 'Elderberry is a woody shrub with paired leaves; water hemlock is a soft plant that dies back in winter.',
   'pokeweed': 'Pokeweed berries are larger and flattened, in long drooping strings on a soft magenta-stemmed plant.',
   'red-elderberry': 'Red elderberry has dome-shaped flower clusters and red berries in early summer.'})
e('saskatoon', 'Amelanchier alnifolia', ['Saskatoon serviceberry', 'Juneberry'], 'starter',
  ['Shrub or small tree, 3 to 15 feet.',
   'Round to oval leaves toothed mainly near the tip.',
   'White star flowers in spring; purple-blue berries like small apples with a crown at the end.'],
  'Berries raw or dried. Seeds contain small amounts of cyanide-forming compounds: do not grind them.',
  'Prairies, coulees and woods edges of the Plains, West and Alaska.')
e('downy-serviceberry', 'Amelanchier arborea', ['Downy serviceberry', 'Juneberry', 'Shadbush'], 'starter',
  ['Small tree with smooth grey bark striped with fine lines.',
   'Oval finely toothed leaves, downy when young.',
   'White flowers in early spring; dark purple berries in June.'],
  'Berries raw or cooked.', 'Woods of the East and Midwest.')
e('chokecherry', 'Prunus virginiana', ['Chokecherry'], 'caution',
  ['Shrub or small tree with grey bark.',
   'Oval leaves with fine SHARP teeth.',
   'Long cylinder-shaped clusters of white flowers; dark red to black cherries hanging in strings.'],
  'Ripe fruit cooked or in jelly, pits removed. Pits, leaves (especially wilted) and bark contain cyanide-forming compounds: do not crush or eat the pits.',
  'Fence rows, coulees and woods edges in nearly every state.',
  {'common-buckthorn': 'Buckthorn berries cluster tight against the twig, not in hanging strings, and buckthorn often has a thorn at the twig tip.'})
e('american-plum', 'Prunus americana', ['American plum', 'Wild plum'], 'caution',
  ['Thicket-forming shrub or small tree, sometimes thorny twigs.',
   'Oval sharply toothed leaves.',
   'White flowers before leaves; red-orange to red plums, 1 inch.'],
  'Ripe fruit raw or cooked. Do not crack or eat the pits (cyanide-forming).',
  'Thickets, fence rows and stream banks of the East, Midwest and Plains.')
e('black-cherry', 'Prunus serotina', ['Black cherry', 'Wild black cherry'], 'caution',
  ['Tree with dark bark in rough scales like burnt potato chips; young bark with horizontal lines.',
   'Narrow glossy leaves with fine incurved teeth and often rusty hairs along the midrib beneath.',
   'Hanging strings of small dark purple-black cherries.'],
  'Ripe fruit raw or cooked, pits removed. Leaves (especially wilted), bark and pits contain cyanide-forming compounds.',
  'Woods and fence rows of the East, Midwest and Southwest mountains.',
  {'common-buckthorn': 'Buckthorn berries cluster tight against the twig, not in hanging strings.'},
  groups=['edible', 'firewood'])
e('beach-plum', 'Prunus maritima', ['Beach plum'], 'caution',
  ['Low shrub of coastal dunes.',
   'Oval toothed leaves; white flowers.',
   'Purple to blue plums with a waxy bloom.'],
  'Ripe fruit cooked or raw, pits removed.', 'Coastal dunes from Maine to Maryland.')
e('pawpaw', 'Asimina triloba', ['Pawpaw'], 'starter',
  ['Understory tree, often in patches, with very large drooping oval leaves (6 to 12 inches).',
   'Maroon six-petalled flowers before the leaves.',
   'Green potato-shaped fruit, 3 to 6 inches, yellow custard inside with large brown seeds.'],
  'Ripe fruit flesh raw. Do not eat the seeds or skin. Some people get stomach upset.',
  'Bottomland woods of the East, Midwest and South.')
e('american-persimmon', 'Diospyros virginiana', ['American persimmon'], 'starter',
  ['Tree with dark bark in thick small squares like alligator skin.',
   'Glossy oval leaves.',
   'Orange fruit, 1 to 2 inches, with a four-part cap.'],
  'Fruit raw only when fully soft and ripe, usually after frost; unripe fruit is astringent. Do not eat large amounts of skins and seeds on an empty stomach (stomach blockage).',
  'Old fields, fence rows and woods of the East, South and lower Midwest.', groups=['edible', 'firewood'])
_grape_look = {'moonseed': 'Moonseed has no tendrils, smooth-edged leaves, and one crescent-shaped seed per fruit. Cut a fruit and look at the seed before eating any.',
               'virginia-creeper': 'Virginia creeper leaves have five separate leaflets; grape leaves are single.',
               'pokeweed': 'Pokeweed is an upright plant without tendrils; its berries are in long strings on magenta stems.'}
e('riverbank-grape', 'Vitis riparia', ['Riverbank grape', 'Wild grape'], 'caution',
  ['Woody climbing vine with shreddy bark and forked TENDRILS.',
   'Large heart-shaped leaves with toothed edges and 3 shallow lobes.',
   'Bunches of small blue-black grapes, each with 2 to 4 pear-shaped seeds.'],
  'Ripe grapes raw or cooked; young leaves cooked. Cut a grape and check the seeds before eating.',
  'Stream banks, fence rows and woods edges of the North, Midwest and Plains.', _grape_look)
e('fox-grape', 'Vitis labrusca', ['Fox grape'], 'caution',
  ['Climbing vine with a tendril at almost every leaf.',
   'Leaves with dense rusty or white felt underneath.',
   'Large dark purple grapes with a musky taste.'],
  'Ripe grapes raw or cooked. Check the seeds.', 'Woods edges and thickets of the Northeast and Appalachians.', _grape_look)
e('summer-grape', 'Vitis aestivalis', ['Summer grape'], 'caution',
  ['Climbing vine with tendrils.',
   'Leaves often deeply lobed, with rusty hairs beneath.',
   'Black grapes with a bluish bloom.'],
  'Ripe grapes raw or cooked. Check the seeds.', 'Woods and thickets of the East and South.', _grape_look)
e('muscadine', 'Vitis rotundifolia', ['Muscadine', 'Scuppernong'], 'caution',
  ['Climbing vine with tight bark and simple (unforked) tendrils.',
   'Round glossy leaves with coarse teeth.',
   'Large thick-skinned purple or bronze grapes in small clusters.'],
  'Ripe grapes raw or cooked. Check the seeds.', 'Woods of the Southeast and Gulf Coast.', _grape_look)
e('woods-rose', 'Rosa woodsii', ["Woods' rose", 'Wild rose'], 'starter',
  ['Prickly shrub, 2 to 6 feet.',
   'Leaves of 5 to 9 toothed leaflets.',
   'Pink five-petalled flowers; red rose hips in fall.'],
  'Hips (fruit) raw or for tea; remove the hairy seeds. Petals.', 'Prairies, stream banks and woods edges of the West and Plains.')
e('prairie-rose', 'Rosa arkansana', ['Prairie rose'], 'starter',
  ['Low shrub, 1 to 2 feet, densely prickly.',
   'Leaves of 7 to 11 leaflets; pink flowers; red hips.'],
  'Hips and petals as for woods\' rose.', 'Prairies of the Great Plains and Midwest.')
e('multiflora-rose', 'Rosa multiflora', ['Multiflora rose'], 'starter',
  ['Large arching thorny shrub forming thickets.',
   'Fringed bracts at the base of each leaf stalk.',
   'Clusters of small white flowers; small red hips in clusters.'],
  'Hips and petals. Invasive.', 'Pastures, fence rows and woods edges of the East and Midwest.')
e('rugosa-rose', 'Rosa rugosa', ['Rugosa rose', 'Beach rose'], 'starter',
  ['Dense bristly shrub with wrinkled leaves.',
   'Large pink or white flowers; big tomato-shaped red hips.'],
  'Hips and petals.', 'Coastal dunes of the Northeast and Great Lakes; planted widely.')
e('downy-hawthorn', 'Crataegus mollis', ['Downy hawthorn'], 'caution',
  ['Small tree with long straight thorns.',
   'Broad toothed leaves, downy beneath.',
   'White flowers; red apple-like fruits (haws).'],
  'Fruit raw or cooked. Do not eat the seeds (cyanide-forming).', 'Woods edges and pastures of the Midwest and East.')
e('highbush-cranberry', 'Viburnum opulus var. americanum', ['American highbush cranberry'], 'starter',
  ['Shrub, 6 to 12 feet.',
   'Paired leaves with three maple-like lobes.',
   'Flat clusters of white flowers with large sterile outer flowers; bright red sour berries hanging into winter.'],
  'Berries cooked (sour); raw in quantity upsets the stomach.', 'Moist woods and swamps of the North and Alaska.')
e('nannyberry', 'Viburnum lentago', ['Nannyberry'], 'starter',
  ['Shrub or small tree.',
   'Paired, finely toothed pointed leaves; winged leaf stalks.',
   'Flat white flower clusters; blue-black berries in drooping clusters.'],
  'Ripe berries raw; spit out the flat seed.', 'Woods edges and stream banks of the North and Plains.')
e('silver-buffaloberry', 'Shepherdia argentea', ['Silver buffaloberry'], 'caution',
  ['Thorny shrub, 6 to 15 feet, with SILVERY leaves in pairs.',
   'Small red berries in dense clusters, sour.'],
  'Berries after frost, cooked or raw in small amounts (saponins).', 'Coulees and river breaks of the Plains and West.')
e('american-black-currant', 'Ribes americanum', ['American black currant'], 'starter',
  ['Shrub, 3 to 5 feet, without thorns.',
   'Maple-like three-lobed leaves with yellow resin dots beneath.',
   'Drooping clusters of black berries.'],
  'Berries raw or cooked.', 'Moist woods and stream banks of the North and Plains.')
e('missouri-gooseberry', 'Ribes missouriense', ['Missouri gooseberry'], 'starter',
  ['Shrub, 3 to 5 feet, with sharp spines at the leaf nodes.',
   'Small lobed maple-like leaves.',
   'Smooth berries, green to purple.'],
  'Berries raw or cooked.', 'Woods of the Midwest and Plains.')
e('golden-currant', 'Ribes aureum', ['Golden currant'], 'starter',
  ['Thornless shrub, 3 to 8 feet.',
   'Small three-lobed leaves.',
   'Yellow tube flowers with a spicy scent; berries yellow, red or black.'],
  'Berries raw or cooked.', 'Stream banks and coulees of the West and Plains.')
e('salal', 'Gaultheria shallon', ['Salal'], 'starter',
  ['Evergreen shrub, 1 to 6 feet, often in dense thickets.',
   'Leathery glossy oval leaves, finely toothed.',
   'Pink urn-shaped flowers; dark purple berries.'],
  'Berries raw or cooked.', 'Coastal forests of the Pacific Northwest.')
e('oregon-grape', 'Mahonia aquifolium', ['Oregon grape', 'Hollyleaved barberry'], 'starter',
  ['Evergreen shrub with holly-like spiny leaflets.',
   'Clusters of yellow flowers; blue berries with a waxy bloom.',
   'Yellow inner bark.'],
  'Berries cooked or raw in small amounts (very sour).', 'Forests of the Pacific Northwest and northern Rockies.')
e('maypop', 'Passiflora incarnata', ['Maypop', 'Purple passionflower'], 'starter',
  ['Climbing vine with tendrils.',
   'Three-lobed leaves.',
   'Elaborate purple fringed flowers; egg-sized green fruit that yellows and wrinkles when ripe.'],
  'Pulp of fully ripe fruit raw.', 'Fields, fence rows and roadsides of the Southeast.')
e('eastern-prickly-pear', 'Opuntia humifusa', ['Eastern prickly pear'], 'caution',
  ['Low sprawling cactus with flat pads.',
   'Few large spines and many tiny barbed bristles (glochids).',
   'Yellow flowers; red fruit.'],
  'Young pads and ripe fruit, cooked or raw, after burning or scraping off the tiny bristles; bristles in the mouth and skin are miserable.',
  'Sandy and rocky ground of the East and Midwest.')
e('plains-prickly-pear', 'Opuntia macrorhiza', ['Plains prickly pear', 'Twistspine prickly pear'], 'caution',
  ['Low cactus with flat pads and spines.',
   'Yellow flowers often with red centres; purple fruit.'],
  'Young pads and ripe fruit after removing spines and bristles.', 'Prairies and rocky ground of the Plains and Southwest.')
e('engelmann-prickly-pear', 'Opuntia engelmannii', ['Engelmann prickly pear', 'Cactus apple'], 'caution',
  ['Large bushy cactus with big round pads.',
   'Yellow flowers; purple-red egg-shaped fruit.'],
  'Young pads and ripe fruit after removing spines and bristles.', 'Deserts and grasslands of the Southwest and Texas.')
e('honey-mesquite', 'Prosopis glandulosa', ['Honey mesquite'], 'starter',
  ['Shrubby tree with paired straight thorns.',
   'Leaves divided into two (sometimes four) feathery parts with narrow leaflets.',
   'Long yellow-tan bean pods, sweet when chewed.'],
  'Dry ripe pods ground to flour (avoid mouldy pods). Wood is a top fuel.',
  'Grassland and desert of Texas, Oklahoma, New Mexico and the Southwest.', groups=['edible', 'firewood'])
e('velvet-mesquite', 'Prosopis velutina', ['Velvet mesquite'], 'starter',
  ['Tree with velvety leaflets and paired thorns.',
   'Tan pods.'],
  'Dry ripe pods ground to flour (avoid mouldy pods).', 'Sonoran Desert of Arizona.', groups=['edible', 'firewood'])
e('soapweed-yucca', 'Yucca glauca', ['Soapweed yucca', 'Small soapweed'], 'caution',
  ['Clump of stiff narrow spine-tipped leaves with white threads on the edges.',
   'Tall stalk of creamy bell flowers; green pods.'],
  'Flowers and young pods, cooked. Roots are soap (saponins), not food.', 'Prairies and rocky slopes of the Great Plains.')
e('sea-grape', 'Coccoloba uvifera', ['Sea grape'], 'starter',
  ['Shrub or tree of beaches with large ROUND leathery leaves with red veins.',
   'Hanging bunches of purple grape-like fruits, each with one large seed.'],
  'Ripe fruit raw or in jelly.', 'Beaches of south and central Florida.',
  {'manchineel': 'Manchineel has small apple-like fruit and pointed oval leaves; sea grape has round leathery leaves and bunches of grape-like fruit.'})
e('saw-palmetto', 'Serenoa repens', ['Saw palmetto'], 'starter',
  ['Low palm with fan leaves and saw-toothed leaf stalks.',
   'Olive-sized black fruits.'],
  'Ripe fruit (strong flavour).', 'Pine flatwoods of Florida and the coastal Southeast.')
e('cabbage-palmetto', 'Sabal palmetto', ['Cabbage palmetto', 'Sabal palm'], 'caution',
  ['Palm tree with large fan leaves and a criss-cross pattern of old leaf bases on the trunk.'],
  'The heart (bud) raw or cooked: taking it kills the tree. Emergency food only.', 'Coastal Southeast and Florida.')
e('wintergreen', 'Gaultheria procumbens', ['Wintergreen', 'Teaberry'], 'starter',
  ['Low evergreen plant under 6 inches.',
   'Glossy oval leaves that smell strongly of wintergreen when crushed.',
   'White bell flowers; red berries.'],
  'Berries raw; leaves for tea in moderation (contain methyl salicylate, an aspirin relative; not for people allergic to aspirin).',
  'Acid woods of the Northeast, Appalachians and upper Midwest.',
  {'mountain-laurel': 'Mountain laurel is a large shrub with no wintergreen smell.'})

# ---------------------------------------------------------------- nuts
e('american-hazelnut', 'Corylus americana', ['American hazelnut'], 'starter',
  ['Shrub, 3 to 10 feet, in thickets.',
   'Broad, double-toothed, heart-shaped leaves.',
   'Nuts in a leafy ragged husk, in clusters.'],
  'Nuts raw or roasted.', 'Woods edges and thickets of the East, Midwest and Plains.')
e('beaked-hazelnut', 'Corylus cornuta', ['Beaked hazelnut'], 'starter',
  ['Shrub, 3 to 10 feet.',
   'Double-toothed oval leaves.',
   'Nut in a bristly husk drawn out into a long beak.'],
  'Nuts raw or roasted. Husk bristles irritate skin.', 'Woods of the North, the mountains and the Pacific coast.')
e('black-walnut', 'Juglans nigra', ['Black walnut'], 'starter',
  ['Large tree with dark deeply furrowed bark.',
   'Leaves of 15 to 23 leaflets.',
   'Round green husked nuts, 2 inches, that stain hands brown.'],
  'Nuts raw or roasted, after removing the husk and drying. Discard mouldy nuts.',
  'Bottomland and fence rows of the East, Midwest and Plains.', groups=['edible', 'firewood'])
e('butternut', 'Juglans cinerea', ['Butternut', 'White walnut'], 'starter',
  ['Tree with light grey ridged bark.',
   'Leaves of 11 to 17 leaflets; a fuzzy "mustache" above each leaf scar.',
   'Oblong sticky green husked nuts.'],
  'Nuts raw or roasted. Discard mouldy nuts.', 'Woods of the Northeast and Midwest.')
e('shagbark-hickory', 'Carya ovata', ['Shagbark hickory'], 'starter',
  ['Large tree with grey bark peeling in long loose strips.',
   'Leaves usually of 5 leaflets.',
   'Round nuts in thick green husks that split into four.'],
  'Nuts raw or roasted.', 'Woods of the East and Midwest.', groups=['edible', 'firewood'])
e('pecan', 'Carya illinoinensis', ['Pecan'], 'starter',
  ['Large tree with leaves of 9 to 17 curved leaflets.',
   'Oblong nuts in thin four-winged husks.'],
  'Nuts raw or roasted.', 'River bottoms of the southern Midwest, South and Texas.', groups=['edible', 'firewood'])
_acorn = 'Acorns, shelled and leached of tannin in changes of water until no longer bitter, then roasted or ground to flour.'
_acorn_look = {'ohio-buckeye': 'Buckeye nuts are round, glossy and sit in a leathery husk, not in a scaly cap.',
               'horse-chestnut': 'Horse chestnuts are round and glossy in a spiky husk, not in a scaly cap.'}
e('white-oak', 'Quercus alba', ['White oak'], 'caution',
  ['Large tree with light grey scaly bark.',
   'Leaves with 5 to 9 ROUNDED lobes (no bristle tips).',
   'Oblong acorns in a warty cap.'],
  _acorn, 'Woods of the East and Midwest.', _acorn_look, groups=['edible', 'firewood'])
e('bur-oak', 'Quercus macrocarpa', ['Bur oak'], 'caution',
  ['Large tree with deeply furrowed bark; corky ridges on young twigs.',
   'Leaves with a narrow waist: deep lobes near the middle, broad lobes at the end.',
   'Large acorns in a deep cap with a FRINGED (mossy) edge.'],
  _acorn, 'Prairies, savannas and river bottoms of the Midwest and Plains.', _acorn_look, groups=['edible', 'firewood'])
e('northern-red-oak', 'Quercus rubra', ['Northern red oak'], 'caution',
  ['Large tree; bark with long flat-topped ridges like ski tracks.',
   'Leaves with 7 to 11 POINTED lobes tipped with bristles.',
   'Acorns in a shallow beret-like cap.'],
  _acorn + ' Red-oak acorns are more bitter and need longer leaching.', 'Woods of the East and Midwest.', _acorn_look, groups=['edible', 'firewood'])
e('gambel-oak', 'Quercus gambelii', ['Gambel oak'], 'caution',
  ['Shrub or small tree in thickets on mountain slopes.',
   'Leaves with deep rounded lobes.',
   'Small acorns.'],
  _acorn, 'Foothills and mountains of the Southwest and southern Rockies.', groups=['edible', 'firewood'])
e('american-beech', 'Fagus grandifolia', ['American beech'], 'starter',
  ['Large tree with smooth light-grey bark.',
   'Oval toothed leaves with straight parallel veins, each ending in a tooth; dry leaves stay on in winter.',
   'Small triangular nuts in pairs inside a prickly husk.'],
  'Nuts raw or roasted (large amounts raw upset the stomach).', 'Woods of the East and Midwest.', groups=['edible', 'firewood'])
_chest_look = {'ohio-buckeye': 'Buckeye husks are smooth or warty, not covered in dense needles; buckeye leaves are hand-shaped with 5 leaflets.',
               'yellow-buckeye': 'Buckeye husks are smooth; leaves hand-shaped.',
               'red-buckeye': 'Buckeye husks are smooth; leaves hand-shaped.',
               'california-buckeye': 'Buckeye husks are smooth; leaves hand-shaped.',
               'horse-chestnut': 'Horse chestnut husks have a few short spikes; nuts are big and round; leaves hand-shaped of 7 leaflets.'}
e('american-chestnut', 'Castanea dentata', ['American chestnut'], 'caution',
  ['Mostly sprouts and small trees now (blight).',
   'Long narrow leaves with large hooked teeth.',
   'Husk covered in long sharp needle-like spines, holding 2 or 3 flattened nuts with a pointed tufted tip.'],
  'Nuts roasted or boiled.', 'Woods of the Appalachians and the East (sprouts).', _chest_look)
e('allegheny-chinkapin', 'Castanea pumila', ['Allegheny chinkapin'], 'caution',
  ['Shrub or small tree.',
   'Narrow toothed leaves, whitish-hairy beneath.',
   'Spiny bur with ONE small pointed nut.'],
  'Nuts raw or roasted.', 'Dry woods of the Southeast.', _chest_look)
e('twoneedle-pinyon', 'Pinus edulis', ['Two-needle pinyon', 'Colorado pinyon'], 'starter',
  ['Small rounded pine with needles in bundles of TWO.',
   'Small round cones with large wingless seeds (pine nuts).'],
  'Pine nuts raw or roasted. Wood is good fuel.', 'Plateaus and foothills of Colorado, Utah, New Mexico and Arizona.',
  groups=['edible', 'firewood'])
e('singleleaf-pinyon', 'Pinus monophylla', ['Singleleaf pinyon'], 'starter',
  ['Small pine with needles SINGLE (one per bundle).',
   'Small cones with large wingless seeds.'],
  'Pine nuts raw or roasted.', 'Mountains of Nevada, Utah, eastern California and Arizona.', groups=['edible', 'firewood'])

# ---------------------------------------------------------------- teas, sap and others
e('eastern-white-pine', 'Pinus strobus', ['Eastern white pine'], 'caution',
  ['Large pine with soft blue-green needles in bundles of FIVE.',
   'Long narrow cones (4 to 8 inches).'],
  'Needle tea (vitamin C); inner bark in emergencies. Not during pregnancy. Never use flat single needles: those are yew or hemlock.',
  'Woods of the Northeast, Great Lakes and Appalachians.',
  {'english-yew': 'Yew needles are flat, single and in two rows, with red berries.',
   'japanese-yew': 'Yew needles are flat and single.',
   'pacific-yew': 'Yew needles are flat and single.',
   'canada-yew': 'Yew needles are flat and single.'}, groups=['edible', 'firewood'])
e('sugar-maple', 'Acer saccharum', ['Sugar maple'], 'starter',
  ['Large tree with paired five-lobed leaves with smooth-edged lobes and U-shaped notches.',
   'Paired winged seeds.'],
  'Sap in late winter, drunk fresh or boiled down to syrup (it takes many gallons of sap for one of syrup).',
  'Woods of the Northeast and Midwest.', groups=['edible', 'firewood'])
e('paper-birch', 'Betula papyrifera', ['Paper birch'], 'starter',
  ['Tree with chalky white bark peeling in papery sheets.',
   'Oval double-toothed leaves.'],
  'Sap in early spring, drunk fresh or boiled down. Bark is excellent tinder.',
  'Northern forests, the mountains and Alaska.', groups=['edible', 'firewood'])
e('spicebush', 'Lindera benzoin', ['Northern spicebush'], 'starter',
  ['Shrub, 6 to 12 feet, in moist woods.',
   'Smooth oval leaves; twigs and leaves smell spicy-lemony when scratched.',
   'Tiny yellow flowers before leaves; glossy red oval berries.'],
  'Twig and leaf tea; dried berries as a spice.', 'Moist woods of the East and Midwest.')
e('staghorn-sumac', 'Rhus typhina', ['Staghorn sumac'], 'starter',
  ['Shrub or small tree with VELVETY branches like deer antlers.',
   'Leaves of 11 to 31 TOOTHED leaflets.',
   'UPRIGHT cone-shaped clusters of fuzzy RED berries.'],
  'Red berry clusters soaked in cold water for a lemonade-like drink (strain the hairs).',
  'Dry open ground of the Northeast and Great Lakes.',
  {'poison-sumac': 'Poison sumac has smooth-edged leaflets, DROOPING WHITE berries, and grows in swamps.'})
e('smooth-sumac', 'Rhus glabra', ['Smooth sumac'], 'starter',
  ['Shrub with smooth hairless branches.',
   'Leaves of 11 to 31 toothed leaflets, white beneath, scarlet in fall.',
   'Upright clusters of fuzzy red berries.'],
  'Red berry clusters soaked in cold water for a drink.', 'Prairies, roadsides and woods edges in every lower-48 state.',
  {'poison-sumac': 'Poison sumac has smooth-edged leaflets and drooping white berries in swamps.'})
e('fragrant-sumac', 'Rhus aromatica', ['Fragrant sumac', 'Skunkbush'], 'starter',
  ['Low shrub, 2 to 6 feet.',
   'Leaves of THREE leaflets, the middle one without a long stalk; smell strong when crushed.',
   'Small clusters of fuzzy RED berries.'],
  'Red berries soaked in cold water for a drink.', 'Prairies, rocky slopes and woods edges across most of the country.',
  {'poison-ivy': 'Poison ivy\'s middle leaflet sits on a longer stalk and its berries are whitish, not red and fuzzy.',
   'western-poison-ivy': 'Poison ivy berries are whitish; fragrant sumac berries are red and fuzzy.'})
e('american-basswood', 'Tilia americana', ['American basswood', 'Linden'], 'starter',
  ['Large tree with big lopsided heart-shaped toothed leaves.',
   'Fragrant cream flowers hanging from a long leafy strap; small round nutlets.'],
  'Young leaves raw; flowers for tea.', 'Woods of the East, Midwest and Plains.', groups=['edible', 'firewood'])
e('eastern-redbud', 'Cercis canadensis', ['Eastern redbud'], 'starter',
  ['Small tree with heart-shaped smooth leaves.',
   'Magenta-pink pea flowers along bare branches in early spring.'],
  'Flowers raw; very young pods cooked.', 'Woods edges of the East, South and lower Midwest.')
e('chia', 'Salvia columbariae', ['Chia', 'Desert chia'], 'starter',
  ['Low annual with deeply cut wrinkled leaves at the base.',
   'Round spiky whorls of blue flowers stacked along the stalk.'],
  'Seeds raw or soaked.', 'Deserts and dry slopes of California, Arizona and Nevada.')
e('yaupon', 'Ilex vomitoria', ['Yaupon holly'], 'starter',
  ['Evergreen shrub with small oval leaves with rounded teeth.',
   'Red berries (do not eat the berries).'],
  'Leaves dried and roasted for a caffeinated tea. Berries are poisonous.', 'Coastal plain of the Southeast and east Texas.')
