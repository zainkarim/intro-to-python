# define a graph node
class GraphNode:
    def __init__(self, adjacent, data):
        self.data = data
        self.adjacent = adjacent
        
    def is_leaf(self):
        return( len(self.adjacent) == 0 )
        
    def __str__(self):
        return( self.data )
      
# Parsing the line
def parse_line(line):
    parts = line.split("|")
    node_name = parts[0].strip()
    adjacent_nodes = parts[1].split(",") if parts[1] else []
    text = parts[2].strip()

    return node_name, adjacent_nodes, text

# load the storty from the raw-text file     
def load_story(filename):
    node_dict = {}
    file = open(filename, "r")    
    for l in file:
        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            node_name, adjacent_nodes, text = parse_line(l)   
            node = GraphNode(adjacent_nodes, text)
            node_dict[node_name] = node

    file.close()
    return( node_dict )

# play the game
def play_story(story_dict):    
    story_node = story_dict["START"]
    print(story_node)

    while not story_node.is_leaf():
        choice_input = input("Your choice (a, b, c, ...): ").lower()
        choice = ord(choice_input) - ord('a')
        story_node = story_dict[ story_node.adjacent[choice] ]
        print(story_node)

    print("THE END")

story_dict = load_story("story.txt") # load story
play_story(story_dict) # play the game

