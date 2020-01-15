import networkx as nx
from myFunc import *
tag_PR = '4a'
tag_ALGO = 'random_graph'
fin_gexf = 'data/Graph_atp_match_2017.gexf'
#  fout_top10_csv = 'output/degree_top10.csv'
#  fout_gexf = 'output/' +  tag_ALGO + '.gexf'

G = nx.read_gexf(fin_gexf)
dict_degree = nx.degree_centrality(G)
#  node_degree1 = nx.degree(G, ('RAFAEL-NADAL'), weight='weight')
#  node_degree1 = nx.degree(G, ('RAFAEL-NADAL'))
list_degree = []
for node in list(G.nodes()):
    list_degree.append(nx.degree(G,node, weight='weight'))
node_size = G.order()
avg_degree = sum(list_degree)/node_size
prob = avg_degree/(node_size - 1)
print(list_degree)
print(node_size)
print(avg_degree)
print(prob)


#  gnp_random_graph(n, p, seed=None, directed=False)
rG = nx.gnp_random_graph(node_size, prob)

fout_gexf ='output/' +  tag_ALGO + '_prob_' + str(round(prob,3)) + '.gexf'
nx.write_gexf(rG, fout_gexf)