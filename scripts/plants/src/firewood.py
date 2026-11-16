# Common firewood trees of the United States with burn quality.
#
# heat:  high   = dense hardwoods; the most heat per cord (Extension "high" class)
#        medium = moderate density
#        low    = light woods; quick hot fires, short burns, kindling
# The class is the heat-per-cord grouping used in university Extension firewood tables
# (University of Missouri G5450) and follows wood density in the USDA Forest Products Laboratory
# Wood Handbook. It is coarse on purpose: moisture matters more than species (season wood until
# it is below about 20 percent moisture; EPA Burn Wise).
# season: rough months to dry after splitting (split, stacked, covered, off the ground).
# notes:  splitting, sparks, smoke, smell, hazards.

F = []
def f(key, sci, common, heat, id, notes, habitat, season='12', src=None, groups=None, use='', look=None, **kw):
    F.append(dict(key=key, sci=sci, common=common, group='firewood', groups=groups or ['firewood'], kind='plant',
                  burn=dict(heat=heat, season_months=season, notes=notes), id=id, use=use, habitat=habitat,
                  look=look or {}, src=src or ['plants', 'missouri-wood-fuel', 'fpl-wood-handbook', 'silvics', 'feis'], **kw))

# ---------------------------------------------------------------- oaks
f('post-oak', 'Quercus stellata', ['Post oak'], 'high',
  ['Leaves with a cross shape: two large square middle lobes.', 'Rough grey bark; small acorns.'],
  'Long hot coals. Seasons slowly.', 'Dry upland woods of the South, lower Midwest and Texas.', '18-24')
f('southern-live-oak', 'Quercus virginiana', ['Southern live oak'], 'high',
  ['Huge spreading evergreen tree, often draped with Spanish moss.', 'Leathery oval leaves, dark and shiny.'],
  'Very dense, very hot, hard to split.', 'Coastal Southeast and Texas.', '18-24')
f('oregon-white-oak', 'Quercus garryana', ['Oregon white oak', 'Garry oak'], 'high',
  ['Leaves with deep rounded lobes, leathery.', 'Grey furrowed bark.'],
  'The best hardwood fuel of the Pacific Northwest.', 'Valleys and foothills of Washington, Oregon and California.', '18-24')
f('water-oak', 'Quercus nigra', ['Water oak'], 'high',
  ['Leaves spatula-shaped, wider at the tip, sometimes three-lobed.', 'Smooth grey bark when young.'],
  'Good fuel; rots fast if left on the ground.', 'Bottomlands and towns of the Southeast.', '12-18')
# white, bur, red and Gambel oak are in edible.py with groups ['edible', 'firewood']
# ---------------------------------------------------------------- hickories and walnuts
f('bitternut-hickory', 'Carya cordiformis', ['Bitternut hickory'], 'high',
  ['Bright SULPHUR-YELLOW winter buds.', 'Leaves of 7 to 11 slender leaflets.', 'Thin-husked bitter nuts (not food).'],
  'Very hot, long burning. Bitter nuts are not food.', 'Woods of the East and Midwest.', '12-18')
f('mockernut-hickory', 'Carya tomentosa', ['Mockernut hickory'], 'high',
  ['Leaves of 7 to 9 leaflets with fuzzy undersides and a fragrant smell.', 'Tight furrowed bark.'],
  'Among the hottest North American woods.', 'Woods of the East and South.', '12-18')
# ---------------------------------------------------------------- ashes, maples
f('white-ash', 'Fraxinus americana', ['White ash'], 'high',
  ['Paired leaves of 5 to 9 leaflets, whitish beneath.', 'Bark in a tight diamond pattern.'],
  'Splits easily and burns well even when only partly seasoned. Many ash trees are dying of emerald ash borer: abundant fuel, but do not move ash wood out of the area.',
  'Woods of the East and Midwest.', '6-12')
f('green-ash', 'Fraxinus pennsylvanica', ['Green ash'], 'medium',
  ['Paired leaves of 5 to 9 leaflets, green on both sides.', 'Bark in a diamond pattern.', 'Paddle-shaped winged seeds in clusters.'],
  'Splits easily, burns well; one of the most common shelterbelt and street trees. Emerald ash borer: do not move ash wood.',
  'River bottoms, shelterbelts and towns of the East, Midwest and Plains.', '6-12')
f('red-maple', 'Acer rubrum', ['Red maple'], 'medium',
  ['Paired three-lobed leaves with toothed edges and V-shaped notches; red stems.', 'Red flowers in early spring.'],
  'Good general fuel.', 'Woods and swamps of the East.', '12')
f('silver-maple', 'Acer saccharinum', ['Silver maple'], 'medium',
  ['Paired leaves deeply cut into five lobes, silvery beneath.', 'Shaggy grey bark on older trees.'],
  'Moderate heat; brittle trees drop many limbs in storms.', 'River bottoms and towns of the East and Midwest.', '12')
f('box-elder', 'Acer negundo', ['Box elder', 'Boxelder maple', 'Ash-leaved maple'], 'low',
  ['Paired leaves of 3 to 5 coarsely toothed leaflets (young ones look like poison ivy).', 'Green or purple-white twigs.', 'Paired winged seeds in drooping clusters.'],
  'Light wood; quick fires, short burns.', 'River bottoms, shelterbelts and towns in nearly every state.', '6-12',
  look={'poison-ivy': 'Box elder leaves grow in PAIRS opposite each other; poison ivy leaves alternate.'})
f('bigleaf-maple', 'Acer macrophyllum', ['Bigleaf maple'], 'medium',
  ['Paired leaves up to 12 inches across with five deep lobes.', 'Moss-covered trunks in wet forests.'],
  'The main hardwood fuel in western Oregon and Washington.', 'Pacific coast forests.', '12')
# ---------------------------------------------------------------- beech, birch, cherry, locusts
f('yellow-birch', 'Betula alleghaniensis', ['Yellow birch'], 'high',
  ['Bronze-yellow bark peeling in thin curls.', 'Twigs smell of wintergreen when scratched.'],
  'Hot fire; the curling bark lights even when wet.', 'Northern hardwood forests and the Appalachians.', '12')
f('honey-locust', 'Gleditsia triacanthos', ['Honey locust'], 'high',
  ['Trunk often armed with large branched thorns (planted forms thornless).', 'Leaves of many small leaflets.', 'Long twisted flat brown pods.'],
  'Hot and long-burning.', 'Bottomlands, pastures and towns of the East, Midwest and Plains.', '12',
  look={'kentucky-coffeetree': 'Coffeetree pods are short, thick and leathery; honey locust pods are long, thin and twisted.'})
f('osage-orange', 'Maclura pomifera', ['Osage orange', 'Hedge apple'], 'high',
  ['Thorny tree with orange-brown furrowed bark and bright yellow-orange wood.', 'Large green wrinkled softball-sized fruits.'],
  'One of the hottest woods; throws many sparks: use a screened stove, not an open fire indoors.', 'Hedgerows of the southern Plains and Midwest; planted widely.', '12')
f('hackberry', 'Celtis occidentalis', ['Common hackberry'], 'medium',
  ['Grey bark covered with corky warts and ridges.', 'Leaves lopsided at the base, toothed, three main veins.', 'Pea-sized purple-brown berries.'],
  'Moderate heat; splits easily.', 'River bottoms, woods and towns of the East, Midwest and Plains.', '12',
  groups=['firewood', 'edible'], use='Fruit raw, or crushed whole (seed and all) into a paste.')
# ---------------------------------------------------------------- elms, cottonwoods, willows
f('american-elm', 'Ulmus americana', ['American elm'], 'medium',
  ['Vase-shaped tree.', 'Lopsided oval double-toothed leaves.', 'Bark in criss-crossing ridges; cut bark shows alternating brown and white layers.'],
  'Interlocked grain makes it very hard to split; split in deep cold. Dead (Dutch elm disease) standing trees are often already dry.',
  'River bottoms and towns of the East, Midwest and Plains.', '12')
f('siberian-elm', 'Ulmus pumila', ['Siberian elm'], 'medium',
  ['Small, narrow, singly-toothed elm leaves, nearly even at the base.', 'Rough grey bark; brittle limbs.'],
  'Hard to split; moderate heat. Invasive: cut freely.', 'Shelterbelts, towns and pastures of the Plains and West.', '12')
f('eastern-cottonwood', 'Populus deltoides', ['Eastern cottonwood', 'Plains cottonwood'], 'low',
  ['Huge tree along rivers.', 'Triangular coarse-toothed leaves on flattened stalks that flutter.', 'Cottony seed fluff in early summer.'],
  'Light, quick-burning; wet when cut and smells when green. Good for spring and fall fires.',
  'River bottoms, shelterbelts and towns of the East, Midwest and Plains.', '12')
f('fremont-cottonwood', 'Populus fremontii', ['Fremont cottonwood'], 'low',
  ['Large tree of desert streams.', 'Triangular coarse-toothed leaves.'],
  'Light, quick-burning.', 'Streams and washes of the Southwest and California.', '12')
f('black-cottonwood', 'Populus balsamifera ssp. trichocarpa', ['Black cottonwood'], 'low',
  ['Tall tree with narrow-oval leaves, dark above and whitish beneath.', 'Sticky fragrant buds.'],
  'Light, quick-burning.', 'Rivers of the Pacific Northwest, northern Rockies and Alaska.', '12')
f('quaking-aspen', 'Populus tremuloides', ['Quaking aspen'], 'low',
  ['Smooth white to greenish bark with black scars.', 'Round finely toothed leaves on flat stalks that tremble in any breeze.'],
  'Light, low smoke, few sparks; burns fast.', 'Mountains of the West, the North and Alaska.', '6-12')
f('black-willow', 'Salix nigra', ['Black willow'], 'low',
  ['Tree of stream banks, often leaning, with several trunks.', 'Long narrow finely toothed leaves.'],
  'Light, quick-burning; poor heat.', 'Stream banks of the East, Midwest and Plains.', '12')
# ---------------------------------------------------------------- other hardwoods
f('american-sycamore', 'Platanus occidentalis', ['American sycamore'], 'medium',
  ['Bark peeling in patches, leaving a white, green and tan camouflage pattern.', 'Large maple-like leaves.', 'Round seed balls hanging on long stalks.'],
  'Moderate heat; very hard to split.', 'Stream banks of the East and Midwest.', '12')
f('sweetgum', 'Liquidambar styraciflua', ['Sweetgum'], 'medium',
  ['Star-shaped leaves with five pointed lobes.', 'Spiky round seed balls.', 'Corky wings on some twigs.'],
  'Moderate heat; hard to split.', 'Woods and towns of the Southeast.', '12')
f('tuliptree', 'Liriodendron tulipifera', ['Tuliptree', 'Yellow poplar'], 'low',
  ['Very tall straight trunk.', 'Leaves with four lobes and a squared-off notched tip, like a tulip outline.', 'Green-orange tulip-like flowers.'],
  'Light; good kindling and shoulder-season wood.', 'Woods of the East and Appalachians.', '6-12')
f('eastern-hophornbeam', 'Ostrya virginiana', ['Eastern hophornbeam', 'Ironwood'], 'high',
  ['Small understorey tree with shreddy bark in narrow vertical strips.', 'Double-toothed birch-like leaves.', 'Hop-like papery seed clusters.'],
  'Among the densest woods; very hot. Small trunks.', 'Woods of the East, Midwest and Plains.', '12')
f('american-hornbeam', 'Carpinus caroliniana', ['American hornbeam', 'Musclewood'], 'high',
  ['Small tree with smooth grey bark rippled like flexed muscle.', 'Double-toothed leaves.'],
  'Dense, hot; small trunks.', 'Stream banks and moist woods of the East.', '12')
f('black-tupelo', 'Nyssa sylvatica', ['Black tupelo', 'Black gum'], 'medium',
  ['Glossy oval leaves, scarlet in fall.', 'Bark in blocky alligator-like ridges; branches at right angles.'],
  'Interlocked grain: very hard to split.', 'Woods and swamps of the East and South.', '12')
f('pacific-madrone', 'Arbutus menziesii', ['Pacific madrone'], 'high',
  ['Smooth orange-red bark peeling in thin sheets.', 'Glossy evergreen leathery leaves.', 'Red-orange berries.'],
  'Dense and hot.', 'Coastal forests of California, Oregon and Washington.', '12')
f('tanoak', 'Notholithocarpus densiflorus', ['Tanoak'], 'high',
  ['Evergreen leaves with straight veins ending in teeth, whitish-fuzzy beneath.', 'Acorns in a bristly cap.'],
  'Dense, hot fuel. Sudden oak death: do not move wood out of infested counties.', 'Coastal forests of California and southwest Oregon.', '12')
f('red-alder', 'Alnus rubra', ['Red alder'], 'medium',
  ['Smooth grey bark, often with white lichen patches.', 'Oval toothed leaves with rolled-under edges.', 'Small woody cone-like catkins.'],
  'Burns cleanly; the Northwest\'s common firewood, used for smoking fish.', 'Moist lowlands of the Pacific coast.', '6-12')
f('russian-olive', 'Elaeagnus angustifolia', ['Russian olive'], 'medium',
  ['Thorny tree with narrow SILVERY leaves.', 'Small silvery-yellow olive-like fruits.'],
  'Moderate to good heat. Invasive: cut freely; watch the thorns.', 'River bottoms and shelterbelts of the West and Plains.', '12')
f('curlleaf-mountain-mahogany', 'Cercocarpus ledifolius', ['Curl-leaf mountain mahogany'], 'high',
  ['Evergreen shrub or small tree with narrow leathery leaves rolled under at the edges.', 'Seeds with long feathery twisted tails.'],
  'Extremely dense; burns very hot and long.', 'Dry mountain slopes of the Great Basin and Rockies.', '12')
f('desert-ironwood', 'Olneya tesota', ['Desert ironwood'], 'high',
  ['Grey-green tree of desert washes with small leaflets and paired thorns.', 'Lavender pea flowers in spring.'],
  'Very dense; burns hot. Protected in places: use dead wood only.', 'Sonoran Desert of Arizona and California.', '12')
f('black-locust-fw', 'Robinia pseudoacacia', ['Black locust'], 'high',
  [], 'Among the best firewoods: hot, long-burning, rot-resistant. Throws sparks. Bark and seeds are poisonous (see the deadly list).',
  '', '12', alias_of='black-locust')
# ---------------------------------------------------------------- conifers
f('eastern-redcedar', 'Juniperus virginiana', ['Eastern redcedar'], 'medium',
  ['Narrow evergreen with scale-like leaves (prickly needles on young growth).', 'Reddish shreddy bark; fragrant red heartwood.', 'Small blue waxy berry-like cones.'],
  'Lights easily and smells pleasant; pops and throws sparks. Good kindling.', 'Pastures, fence rows and prairies of the East, Midwest and Plains.', '6-12')
f('utah-juniper', 'Juniperus osteosperma', ['Utah juniper'], 'medium',
  ['Bushy evergreen with scale-like leaves.', 'Shreddy grey bark.', 'Blue-brown berry-like cones.'],
  'Good heat, aromatic; sparks.', 'Pinyon-juniper woodland of the Great Basin and Colorado Plateau.', '6-12')
f('rocky-mountain-juniper', 'Juniperus scopulorum', ['Rocky Mountain juniper'], 'medium',
  ['Small evergreen with scale-like leaves.', 'Blue waxy berry-like cones.'],
  'Good heat, aromatic; sparks.', 'Rocky slopes and breaks of the Rockies and western Plains.', '6-12')
_pine = 'Resinous: lights fast and burns hot but short; seasoned wood keeps creosote down. Fat pine (resin-soaked stumps) is the best fire-starter there is.'
f('ponderosa-pine', 'Pinus ponderosa', ['Ponderosa pine'], 'medium',
  ['Long needles in bundles of 2 or 3.', 'Orange-brown bark in large plates (smells of vanilla on warm days).'], _pine,
  'Mountains and foothills across the West, the Black Hills and Pine Ridge.', '6-12')
f('lodgepole-pine', 'Pinus contorta', ['Lodgepole pine'], 'medium',
  ['Straight thin trunks in dense stands.', 'Needles in bundles of TWO.', 'Small cones that stay closed on the tree.'], _pine,
  'Mountains of the West and Alaska.', '6-12')
f('loblolly-pine', 'Pinus taeda', ['Loblolly pine'], 'medium',
  ['Needles in bundles of THREE, 6 to 9 inches.', 'Prickly cones.'], _pine, 'Woods and plantations of the Southeast.', '6-12')
f('longleaf-pine', 'Pinus palustris', ['Longleaf pine'], 'medium',
  ['Very long needles (8 to 18 inches) in bundles of three.', 'Large cones; young trees look like a grass clump.'], _pine,
  'Coastal plain of the Southeast.', '6-12')
f('shortleaf-pine', 'Pinus echinata', ['Shortleaf pine'], 'medium',
  ['Short needles in bundles of 2 or 3.', 'Bark with small resin pockets.'], _pine, 'Woods of the South and Ozarks.', '6-12')
f('slash-pine', 'Pinus elliottii', ['Slash pine'], 'medium',
  ['Needles in bundles of 2 and 3.', 'Glossy cones on short stalks.'], _pine, 'Flatwoods of Florida and the Gulf Coast.', '6-12')
f('jack-pine', 'Pinus banksiana', ['Jack pine'], 'medium',
  ['Short twisted needles in bundles of two.', 'Curved cones that stay closed until fire.'], _pine, 'Sandy ground of the upper Great Lakes.', '6-12')
f('red-pine', 'Pinus resinosa', ['Red pine'], 'medium',
  ['Long needles in bundles of two that SNAP cleanly when bent.', 'Reddish plated bark.'], _pine, 'Northern forests of the Great Lakes and Northeast.', '6-12')
f('douglas-fir', 'Pseudotsuga menziesii', ['Douglas-fir'], 'medium',
  ['Single needles all round the twig.', 'Cones with three-pointed bracts sticking out like a mouse\'s hind feet and tail.', 'Thick corky bark on old trees.'],
  'The best softwood fuel: dense for a conifer, burns hot.', 'Forests of the West.', '6-12')
f('engelmann-spruce', 'Picea engelmannii', ['Engelmann spruce'], 'low',
  ['Sharp four-sided single needles.', 'Papery thin-scaled cones.'], 'Light; pops and sparks. Good kindling.', 'High mountains of the West.', '6-12')
f('white-spruce', 'Picea glauca', ['White spruce'], 'low',
  ['Sharp four-sided needles that smell skunky when crushed.', 'Slender cones.'], 'Light; sparks.', 'Northern forests, Alaska, and the Black Hills.', '6-12')
f('black-spruce', 'Picea mariana', ['Black spruce'], 'low',
  ['Narrow spire-shaped tree in bogs.', 'Short blunt needles; small round cones clustered at the top.'], 'Light; sparks.', 'Bogs of the far North and Alaska.', '6-12')
f('subalpine-fir', 'Abies lasiocarpa', ['Subalpine fir'], 'low',
  ['Narrow spire-shaped tree.', 'Flat blunt needles turning upward; resin blisters on the bark.', 'Upright purple cones.'], 'Light; poor heat.', 'High mountains of the West.', '6-12')
f('balsam-fir', 'Abies balsamea', ['Balsam fir'], 'low',
  ['Flat needles with two white bands beneath, fragrant.', 'Resin blisters on smooth bark.'], 'Light; poor heat; good kindling.', 'Northern forests of the Northeast and Great Lakes.', '6-12')
f('white-fir', 'Abies concolor', ['White fir'], 'low',
  ['Long flat blue-green needles curving upward.', 'Smooth grey bark with resin blisters.'], 'Light.', 'Mountains of the Southwest, California and the Great Basin.', '6-12')
f('tamarack', 'Larix laricina', ['Tamarack', 'Eastern larch'], 'medium',
  ['Conifer that drops its needles in fall (turns gold).', 'Soft needles in tufts on short spurs.', 'Small cones.'], 'Good heat for a softwood; sparks.', 'Bogs of the North and Alaska.', '6-12')
f('western-larch', 'Larix occidentalis', ['Western larch'], 'medium',
  ['Tall conifer that drops its needles in fall.', 'Soft needles in tufts.'], 'Good heat for a softwood.', 'Mountains of the inland Northwest.', '6-12')
f('eastern-hemlock', 'Tsuga canadensis', ['Eastern hemlock'], 'low',
  ['Short flat needles with two white lines beneath, on tiny stalks.', 'Tiny cones; drooping leader.'],
  'Light; sparks. Not related to poison hemlock (a plant).', 'Cool ravines and forests of the Northeast and Appalachians.', '6-12')
f('western-hemlock', 'Tsuga heterophylla', ['Western hemlock'], 'low',
  ['Short flat needles of different lengths; drooping top.'], 'Light; sparks.', 'Coastal forests of the Pacific Northwest and Alaska.', '6-12')
f('western-redcedar', 'Thuja plicata', ['Western redcedar'], 'low',
  ['Flat sprays of scale-like leaves.', 'Stringy red-brown bark.'], 'Light, pops; superb kindling (splits fine).', 'Wet forests of the Pacific Northwest and northern Rockies.', '6')
f('northern-white-cedar', 'Thuja occidentalis', ['Northern white-cedar', 'Arborvitae'], 'low',
  ['Flat sprays of scale-like leaves.', 'Shreddy grey bark.'], 'Light, pops; kindling.', 'Swamps and limestone of the Great Lakes and Northeast.', '6')
