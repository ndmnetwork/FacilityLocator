from enum import Enum


class Service(Enum):
    BCONS = 'Bcons'
    PCONS_PIPES = 'Pcons & Pipes'
    SCONS = 'Scons'
    OIL = 'Oil'
    PETROL = 'Petrol'
    HEAVY_OIL = 'Heavy Oil'
    ENRICHED_OIL = 'Enriched Oil'
    CAMS = 'Cams'
    PAMS = 'Pams'
    SAMS = 'Sams'
    HAMS = 'Hams'
    NAMS = 'Nams'
    CONCRETE = 'Concrete'
    METAL_BEAMS = 'Metal Beams'
    BARBED_WIRE = 'Barbed Wire'
    SANDBAGS = 'Sandbags'
    FLAME_BARREL = 'Flame Barrel'
    ROCKET = 'Rocket'
    FLAME_ROCKET = 'Incendiary Rocket'
    MM_300 = '300mm'
    MM_250 = '250mm'
    MM_150 = '150mm'
    MM_120 = '120mm'
    MM_94_5 = '94.5mm'
    MM_75 = '75mm'


class VehicleService(Enum):
    MODIFICATION_CENTER = 'Modification Center'
    LIGHT_ASSEMBLY = 'Light Assembly'
    LIGHT_ASSEMBLY_MP = 'Light Assembly (Motor Pool)'
    LIGHT_ASSEMBLY_RF = 'Light Assembly (Rocket Factory)'
    LIGHT_ASSEMBLY_FS = 'Light Assembly (Field Station)'
    LIGHT_ASSEMBLY_TF = 'Light Assembly (Tank Factory)'
    LIGHT_ASSEMBLY_WP = 'Light Assembly (Weapons Platform)'
    LARGE_ASSEMBLY = 'Large Assembly'
    LARGE_ASSEMBLY_T = 'Large Assembly (Train)'
    LARGE_ASSEMBLY_HT = 'Large Assembly (Heavy Tank)'


class Region(Enum):
    KALOKAI = ('Kalokai', ('Baccae Ridge', 'Bleary', 'Camp Tau', 'Clarity Meadow', 'Hallow', 'Ichorus Amphitheatre', 'Lost Greensward', "Night's Regret", 'Sourtooth', 'South March', 'Sweethearth', 'The Stumble', 'The Vineroad', 'Vinum Rillet'))
    RED_RIVER = ('Red River', ('Camp Upsilon', 'Cannonsmoke', 'Climb', 'Fort Matchwood', 'Fragment Knolls', 'Gunpowder Lane', 'Judicium', 'Minos', 'Penance', 'Perish', 'Red Crossing', 'The Red River', 'Twelve Drops', 'Victoria Hill'))
    ACRITHIA = ('Acrithia', ("Astero's Spear", 'Camp Omicron', 'Duelling Kegs', 'Fated Heel', 'Final March', 'Heir Apparent', 'Legion Ranch', 'Nereid Keep', 'Patridia', 'Riverlands', 'Swordfort', 'The Brinehold', 'Thetus Ring', 'Weary Slumber'))
    ASH_FIELDS = ('Ash Fields', ('Ashtown', 'Camp Omega', 'Cometa', 'Electi', "Gunslinger's Pass", 'Mount Blackmoth', 'Mount Brimstone', 'Omega Valley', 'Sootflow', 'Tar Creek', 'The Ashfort', 'The Calamity', 'The Red River', 'The Stillness', 'Twin Flames', 'Wasteful Calm'))
    TERMINUS = ('Terminus', ('Aspisa', 'Bay of the Ward', 'Bloody Palm Fort', 'Cerberus Wake', 'Dogbone', "Martyr's Fang", 'Rising Loom', 'Sever', "The Legion's Bounty", 'The Phalanx', 'The Respite', 'Therizó', 'Three Siblings', 'Thunder Plains', 'Thunderbolt', "Warlord's Stead", 'Winding Bolas'))
    ORIGIN = ('Origin', ('Arise', 'Cado', 'Dormio', 'Exorior', 'Finis', 'Initium', 'Teichotima', 'Temple Field', "The Dreamer's Road", 'The Echo', 'The Sundering', 'World Star'))
    THE_FINGERS = ('The Fingers', ("Captain's Dread", 'Cavitatis', 'Cementum', 'Fort Barley', "Headsman's Villa", 'Mount Talio', 'Plankhouse', 'Second Man', 'Tears of Tethys', 'The Old Captain', 'The Routed', 'The Tusk', 'The Wary Nymphae', 'Titancall'))
    GREAT_MARCH = ('Great March', ('Camp Senti', 'Dalton Meadow', 'Dendró Field', 'Eristown', 'Fateless Grove', 'Fengari', 'Halting Valley', 'Jack Field', 'Jackboot Creek', 'Legacy Pasture', 'Leto', 'Lionsfort', 'Milowood', 'Mors Range', "Myrmidon's Stay", 'Remnant Acreage', 'Remnant Villa', 'Schala Estate', 'Scrabbling Motte', 'Serpent Charm', 'Sitaria', 'The Black Wing', 'The Great March', 'The Midmarch', 'The River Senti', 'The Spice Road', 'The Swan', 'The White Wing', 'Violet Fields', 'Violethome', 'Zealous Approach'))
    THE_HEARTLANDS = ('The Heartlands', ('18th Sideroad', 'Barronshire ', 'Barronswall', 'Barrony Ranch', 'Barrony Road', 'Cageroad', 'Crater Basin', 'Deeplaw Post', 'Erimos Ranch', 'Fort Providence', 'Greenfield Orchard', "Harvester's Range", 'Janus Field', 'Kos Meadows', 'Loftmire', 'Lower Barrony Field', 'Oleander Fields', 'Oleander Homestead', 'Pandora Compound', 'Proexí', 'Providence Field', 'The Blemish', 'The Breach', 'The Fuming Pen', 'The Orchard Wall', 'The Plough', 'The Rollcage', 'The Salt Crossing', 'Upper Barrony Field', 'Upper Heartlands'))
    SHACKLED_CHASM = ('Shackled Chasm', ('A Careless Net', 'A New Spring', 'Autumn Pyres', 'Final Step', 'Firstmarch', 'Gorgon Grove', 'Hades Ladder', "Legion's Dawn", 'Limewood Holdfast', 'Manky Hills', 'Reflection', 'Savages', 'Silk Farms', "Simo's Run", 'Southreach', 'The Bell Toll', 'The Blue', 'The First Rung', 'The Foolish Maidens', 'The Grave of Erastos', 'The Plunging', 'The Vanguard', "Widow's Web"))
    WESTGATE = ('Westgate', ('Ash Step', 'Candle Hills', 'Cattle March', 'Ceo Highlands', 'Cinder Road', 'Coasthill', 'Coastway', "Cobber's Lane", "Cobber's Lane", 'Ember Hills', "Fand's Chain", 'Fields of Badb', 'Fields of Badb', "Flidais' Pasture", 'Handsome Hideaway', 'Hillcrest', 'Holdfast', 'Inkwell Lane', 'Kardia Road', 'Killian Quarter', 'Kingstone', 'Longstone', "Lord's Mouth", 'Lost Partition', "Rancher's Fast", "Reaver's Cove", 'Sanctified Path', 'Sanctuary', 'Síochána Valley', 'Taswell Point', 'The Aging Ocean', 'The Bulwark', 'The Divide', 'The Gallows', 'The Hem', "The King's Road", "The King's Road", "The Knight's Edge", "Triton's Curse", 'Warden Walk', 'Western Heartlands', 'Westgate Keep', 'Wire Road', 'Wyattwick', "Zeus' Demise"))
    ALLODS_BIGHT = ('Allods Bight', ("A Captain's Repose", "Allod's Children", 'Belaying Trace', 'Blunder Bight', 'Breath of Cetus', 'Gangrenous Hollow', "Harpy's Perch", 'Homesick', "Mercy's Wail", 'Rumhold', 'Scurvyshire', 'The List', 'The Rumroad', 'The Stone Plank', 'The Turncoat', "Titan's End", "Witch's Last Flight"))
    FISHERMANS_ROW = ('Fishermans Row', ('A Lost Sot', 'Arcadia', 'Bident Crossroads', 'Black Well', 'Cat Step', 'Dankana Post', 'Eidolo', 'Fort Ember', "Hangmen's Court", 'Heart of Rites', 'House Roloi', 'Lake Nerites', 'Liberty Hill', 'Oceanwatch', 'Partisan Island', 'Peripti Landing', 'Progonos Watch', 'The Dire Strings', 'The Rite Road', 'The Satyr Stone', 'The Three Sisters', 'Torch of Demeter'))
    TEMPEST_ISLAND = ('Tempest Island', ('Alchimio Estate', 'Cirris Valve', 'Eros Lagoon', 'Isle of Psyche', "Liar's Haven", 'Lost Airchal', 'Plana Fada', 'Reef', 'Sclera', 'Stratos Valve', 'Surge Field', 'Surge Gate', 'The Gale', 'The Iris', 'The Outwood', 'The Rush'))
    UMBRAL_WILDWOOD = ('Umbral Wildwood', ('Adze Crossroads', 'Amethyst', "Atropos' Fate", "Clotho's Refuge", 'Dredgefield', 'Golden Concourse', 'GoldenRoot Ranch', "Hermit's Rest", "Lachesis' Tally ", 'Leatherback Pathway', 'Sentry', 'Steely Fields', 'Stray', 'Terrapin Woods', 'The Dredgewood', 'The Foundry', 'The Frontier', 'The Gap', 'The Strands', 'Thunder Row', 'Thunderfoot', 'Vagrant Bastion', 'Wasting Holt', "Weaver's Trail"))
    LOCH_MOR = ('Loch Mór', ("Bastard's Blade", 'Chattering Prairie', 'Escape', 'Fallen Fields', 'Feirmor', 'Lake Severspring', 'Loch Mor', 'Market Road', "Mercy's Wish", 'Missing Bones', "Moon's Copse", 'Ousterdown', 'Pockfields', 'Rip', 'Tear', 'The Founding Fields', 'The Glean', 'The Reaping Road', 'The Roilfort', 'Tomb of the First', 'Westmarch', "Widow's Wail"))
    THE_DROWNED_VALE = ('The Drowned Vale', ('Bootnap', 'Coaldrifter Stead', 'Eastmarch', 'Esterfal', 'Fleetsfall River', 'Linger', 'Loggerhead', 'Singing Serpents', 'Sop Fields', 'Splinter Pens', "Sprite's Game", 'The Baths', 'The Other Vein', 'The Saltcaps', 'The Turtlerocks', 'The Wash', 'The Willow Wood', 'Vessel', "Wisp's Warning"))
    FARRANAC_COAST = ('Farranac Coast', ("Apollo's Landing", 'Carrion Fields', 'Cora Lushlands', 'Cormac Beach', 'Gulf of the Daughters', 'Hermes Inlet', 'Huskhollow', 'Iuxta Homestead', 'Kardia', 'Liberation Street', "Macha's Keening", 'Mara', 'McCarthy Fields', 'Mooring Dens', 'Pleading Wharf', 'Scarp of Ambrose', 'Scythe', 'Sickle Hill', 'Skeleton Road', 'Sunder Beach', 'Terra', 'The Bay of Artemis', 'The Bone Haft', 'The Heart Road', 'The Iron Beach', 'The Jade Cove', 'The Mirror', 'The Reaping Fields', 'The River Mercy', 'The Snag', 'The Spearhead', 'The Winged Walk', 'Transient Valley', 'Victa'))
    ENDLESS_SHORE = ('Endless Shore', ("Balor's Crown", 'Battered Landing', 'Brackish Point', 'Dannan Ridge', "Dearg's Fang", 'Enduring Wake', 'Iron Junction', "Kelpie's Mane", "Kelpie's Tail", 'Liegehearth', "Merrow's Rest", 'Saltbrook Channel', 'Sídhe Fall', 'The Dannan Coast', 'The Dark Road', 'The Evil Eye', 'The North Star', 'The Old Jack Tar', 'The Overland', 'The Selkie Bluffs', 'The Styx', 'The Whispering Waves', 'Tuatha Watchpost', 'Vulpine Watch', 'Wellchurch', 'Woodbind'))
    THE_OARBREAKER_ISLES = ('The Oarbreaker Isles', ('Barrenson', 'Base Akri', 'Castor', 'Crach Woods', 'Fogwood', 'Gold', 'Grisly Refuge', 'Integrum', 'Kofteri Channel', "Lion's Head", 'Martius', 'Mount Marce', "Neptune's Throne", 'Oasis', 'Obitum', 'Pollux', 'Posterus', 'Reliqua', 'Sandalwood Beach', "Sheep's Head", 'Silver', 'Skelter Course', 'Skull Beach', 'The Conclave', 'The Dirk', 'The Emblem', 'The Ides'))
    GODCROFTS = ('Godcrofts', ('Anchor Beach', 'Argosa', 'Bagh Mòr', "Barreller's Bay", 'Blackwatch', 'Chamil Ravine', 'Den of Thieves', 'Exile', 'Isawa', 'Kolas', 'Lipsia', 'Peripti Depths', 'Perpetua Channel', 'Primus Trames', 'Promithiens', 'Protos', 'Saegio', 'Skodio', 'The Axehead', 'The Dice Road', 'The Fleece Road', 'The Kris Ford', 'The Kris Ford', 'Ursa Trail', 'Vicit Lagoon'))
    DEADLANDS = ('DeadLands', ('Abandoned Ward', 'Biting Tarn', 'Border Concourse', 'Border Thicket', 'Brine Glen', "Callahan's Belt", "Callahan's Boot", "Callahan's Gate", 'Carpal Trail', 'Cemetary Junction', 'Cemetary Lane', 'Coracoid Footpath', 'Crumbling Passage', "Hope's Causeway", "Iron's End", 'Jaspar Range', 'Liberation Point', 'Mandible Crossroads', 'Marrow Copse', 'Mercy Meadow', "Mercy's End", 'Overgrown Pasture', 'Path to the Sun', 'Pommel Annex', "Sun's Hollow", 'Sunhaven Gateway', 'Tarsal Pathway', 'The Abbey Drag', 'The Blade', 'The Boneyard', 'The Crossing', 'The Great March', 'The Iron Passage', 'The Iron Road', 'The Pits', 'The Plaza', 'The Salt Farms', 'The Salt March', 'The Salt Trail', 'The Shorn Fields', 'The Spine', 'The Steppes'))
    THE_LINN_OF_MERCY = ('The Linn of Mercy', ('Blackroad', 'Fort Duncan', 'Gallant Gough Boulevard', 'Hardline', 'Lathair', 'Merciful Strait', 'Mudhole', 'Nathair', 'Outwich Ranch', 'Rotdust', 'Solas Burn', 'The Crimson Gardens', 'The Drone', 'The First Coin', 'The Great Scale', 'The Last Grove', 'The Long Whine', 'The Prairie Bazaar', 'The River Mercy', 'Ulster Falls'))
    MARBAN_HOLLOW = ('Marban Hollow', ('Bleating Plateau', 'Bubble Basin', 'Checkpoint Bua', 'Deepfleet Valley', 'Gaping Maw', 'Lockheed', 'Lockheed Breakers', 'Lughbone Dam', "Maiden's Veil", 'Mount Mac Tire', 'Mox', 'Oster Wall', 'Pilgrimage', 'Sanctum', 'Slender Cove', 'The Claim', 'The Clutch', 'The Curse', 'The Spitrocks'))
    STONECRADLE = ('Stonecradle', ('Buckler Sound', 'Daihbi Point', 'Fading Lights', 'Longing', 'The Cord', 'The Dais', "The Heir's Knife", 'The Loneliest Shore', 'The Long Fast', 'The Pram', 'The Reach', 'The Roiling Comets', 'The Whorl', 'Trammel Pool', "World's End"))
    WEATHERED_EXPANSE = ('Weathered Expanse', ('Bannerwatch', 'Barrowsfield', "Crow's Nest", "Dullahan's Crest", 'Eapoe', 'Foxcatcher', 'Frostmarch', 'Huntsfort', 'Kirkyard', 'Necropolis', 'Port of Rime', "Revenant's Path", 'Rime Wastes', 'Shattered Advance', 'Spirit Watch', 'The Ivory Bank', 'The Ivory Sea', 'The Spear', 'The Stand', 'The Weathered Wall', 'The Weathering Halls', 'Wightwalk', "Wraith's Gate"))
    NEVISH_LINE = ('Nevish Line', ('Blackcoat Way', 'Blinding Stones', 'Grief Mother', 'Mistle Shrine', 'Nevish Trail', 'Plumage', 'Princefal', 'Princefal Burn', 'Tear Road', 'The Aging Ocean', 'The Arrow', 'The Scrying Belt', 'Tomb Father', 'Unruly'))
    MORGENS_CROSSING = ('Morgens Crossing', ('Allsight', "Bastard's Block", "Callum's Descent", 'Crimson Thread', 'Eversus', 'Lividus', 'Quietus', 'Rising Calm', 'The Bastard Sea', 'Ultimus', 'Velian Storm', 'Warmonger Bay'))
    CALLAHANS_PASSAGE = ('Callahans Passage', ("Callahan's Eye", 'Chapel Access', 'Cragsfield', 'Cragsroad', 'Cragstown', 'Crumbling Post', 'Lingering Lashes', 'Lochan', 'Lochan Berth', 'Lost Tops', 'Overlook Hill', 'Scáth Passing', 'Sioc Approach', 'Solas Gateway', 'Solas Gorge', 'Soured Fields', 'The Crumbling Passage', 'The Key', 'The Lance', 'The Latch', 'The Procession', 'The Rust Road', 'The Stern', 'Twisted Mumble', 'Whispering Gulch', 'White Chapel', 'Winding Crag'))
    THE_MOORS = ('The Moors', ('Borderlane', "Gravekeeper's Holdfast", 'Headstone', "Luch's Workshop", "Lyon's Wood", 'MacConmara Barrows', "Moon's Walk", "Morrighan's Grave", 'Ogmaran', 'Reaching River', 'Riverhill', 'Scáth Copse', 'The Cut', 'The Graveyard', 'The Mound', 'The Spade', 'The Wind Hills', 'Wiccwalk', 'Wiccwood'))
    VIPER_PIT = ('Viper Pit', ("Afric's Approach", 'Austriaca River', 'Blackthroat', 'Deadsteps', 'Earl Crowley', "Earl's Welcome", 'Fleck Crossing', 'Fort Viper', 'Hardcaps', 'Kirknell', 'Lake Mioira', 'Moltworth', 'Path of the Charmed', "Serenity's Blight", 'Snakehead Lake', 'The Bloody Bowery', 'The Friars', "The Lady's Lake", 'The Rockaway', 'The Slithering Scales', 'The Tongue', 'Twin Fangs'))
    CALLUMS_CAPE = ('Callums Cape', ("Callum's Keep", 'Camp Hollow', 'Holdout', 'Hollowhill', 'Ire', 'Lookout', 'Naofa', 'Princefal Burn', 'Scouts Jest', 'The Dreg', 'The Gunwall', 'The River Vein', 'Trail of the Dead', 'Valta Downs', 'Vex'))
    CLANSHEAD_VALLEY = ('Clanshead Valley', ('Bramble Field', 'Fallen Crown', 'Fort Ealar', 'Fort Esterwild', 'Fort Windham', 'Lost Orphans', 'Sweetholt', 'Tallowild', "The Bastard's Channel", 'The King', 'The Pike', 'The Weathered Advance', 'Throne of Druiminn'))
    REACHING_TRAIL = ('Reaching Trail', ('Brodytown', 'Camp Eos', 'Caragtais', "Duffy's Farm", "Dugan's Approach", 'Dwyersfield', 'Dwyerstown', 'Elksford', 'Featherfield', "Fisherman's Floe", 'Fort Mac Conaill', 'Harpy', 'Hookhall', 'Humidus', 'Ice Ranch', 'Limestone Holdfast', "Mac Conaill's Pass", 'Mousetrap', 'Nightchurch', 'Pitfall', 'Puncta', 'Reprieve', 'Scorpion', 'The Ark', 'The Bait', 'The Cairns', 'The Chicken Coop', 'The Deckard', 'The Knot', 'The Reaching Heights', 'The Rime Ledge', 'The Rousing Fields', 'The Scar', 'The Squeeze', 'Thýlak', 'Windy Way'))
    SPEAKING_WOODS = ('Speaking Woods', ('Calmland', 'Cursed Court', 'Fort Blather', 'Hush', 'Inari Base', 'Mount Rell', 'Mute', 'Reaching River', 'Rell Foothills', 'Sotto Bank', 'Stem', 'The Filament', 'Tine', 'Wound'))
    HOWL_COUNTY = ('Howl County', ('Austriaca Reservoir', 'Checkpoint Titim', 'Fort Red', 'Fort Rider', 'Great Warden Dam', 'Hungry Wolf', 'Little Lamb', 'Sickleshire', 'Slipgate Outpost', 'Snakewall', 'Teller Farm', 'The Hunting Grounds', 'Viperwalk'))
    BASIN_SIONNACH = ('Basin Sionnach', ('Basin Sionnach', 'Basinhome', 'Cunning Cross', 'Cuttail Station', 'Lamplight', 'Radiant Shore', 'Sess', 'Stoic', 'The Den', 'The Foxfields', 'Torchwood'))
