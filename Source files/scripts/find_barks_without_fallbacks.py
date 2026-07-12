source_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Darkest Dungeon® II\Darkest Dungeon II_Data\StreamingAssets\Localization\Sources"

# Examples:
# 1.
# bark_act_out_start_my_turn_stress_heal_partner=Steady those hands. We shall win this.
# bark_act_out_start_my_turn_stress_heal_partner+highwayman=You're tougher than this. Breathe.

# will output nothing.

# 2.
# bark_act_out_start_my_turn_buff_partner+highwayman=Shoot to kill.
# bark_act_out_start_my_turn_buff_partner+man_at_arms=Show them what you're made of!

# will output bark_act_out_start_my_turn_buff_partner

# 3.
# bark_act_out_rest_item_hate_block+envious+highwayman=You'd love that, I'm sure.
# bark_act_out_rest_item_hate_block+envious+highwayman=Let me cut you off there - no.

# will output bark_act_out_rest_item_hate_block+envious

# 4.
# bark_node_exit_gate+kingdominnsieged+highwayman+beastmen=Keep vigilant at choke points.
# bark_node_exit_gate+kingdominnsieged+highwayman+beastmen=Air's so stagnant. Not a breath of wind.

# will output bark_node_exit_gate+kingdominnsieged


import os

special_markers = {
    "highwayman",
    "man_at_arms",
    "grave_robber",
    "plague_doctor",
    "occultist",
    "jester",
    "leper",
    "hellion",
    "runaway",
    "vestal",
    "flagellant",
}

generic_bases = set()
special_bases = set()

def parse_file(file_path):
    encoding = "utf-8-sig" # to remove \ufeff at the beginning of each file
    with open(file_path, encoding=encoding) as f:
        for line in f:
            line = line.strip()
            key = line.split("=", 1)[0]
            parts = key.split("+")

            # find a special marker
            special_idx = None
            for i, part in enumerate(parts):
                if part in special_markers:
                    special_idx = i
                    break

            if special_idx is None:
                # generic entry
                generic_bases.add(key)
            else:
                # if additional +something are present before the special marker, they count as part of the base.
                # If they are present after special markers, they count as part of special markers.
                base = "+".join(parts[:special_idx])
                special_bases.add(base)

for root, dirs, files in os.walk(source_dir):
    for filename in files:
        file_path = os.path.join(root, filename)
        parse_file(file_path)

missing_generics = sorted(special_bases - generic_bases)
for base in missing_generics:
    print(base)
