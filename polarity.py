import xml.etree.ElementTree as ET

tree = ET.parse('senticnet-2.0/senticnet2.rdf.xml')
root = tree.getroot()

con_pol_pairs = {}
for i in range(len(root)):
    d = {}
    con_pol_pairs[root[i][1].text] = float(root[i][-1].text)


