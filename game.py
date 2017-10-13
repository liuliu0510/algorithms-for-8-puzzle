from anytree import Node, RenderTree
import math

INFINITY = 100000
TRUE = 1
FALSE = -1

"""
#the first case 
rootnode = Node('')
node10 = Node('', parent = rootnode)
node11 = Node('', parent = rootnode)
node20 = Node('4', parent = node10)
node21 = Node('', parent = node10)
node22 = Node('8', parent = node10)
node23 = Node('', parent = node11)
node24 = Node('', parent = node11)
node30 = Node('7', parent = node21)
node31 = Node('9', parent = node21)
node32 = Node('8', parent = node21)
node33 = Node('', parent = node23)
node34 = Node('2', parent = node23)
node35 = Node('6', parent = node23)
node36 = Node('', parent = node24)
node37 = Node('4', parent = node24)
node38 = Node('7', parent = node24)
node39 = Node('', parent = node24)
node40 = Node('3', parent = node33)
node41 = Node('6', parent = node33)
node42 = Node('4', parent = node33)
node43 = Node('9', parent = node36)
node44 = Node('2', parent = node36)
node45 = Node('9', parent = node36)
node46 = Node('6', parent = node39)
node47 = Node('4', parent = node39)
node48 = Node('5', parent = node39)
"""

"""
#the second case
rootnode = Node('')
node10 = Node('', parent = rootnode)
node11 = Node('', parent = rootnode)
node20 = Node('', parent = node10)
node21 = Node('', parent = node10)
node22 = Node('', parent = node10)
node23 = Node('', parent = node11)
node24 = Node('', parent = node11)
node30 = Node('1', parent = node20)
node31 = Node('4', parent = node20)
node32 = Node('3', parent = node21)
node33 = Node('', parent = node21)
node34 = Node('7', parent = node21)
node35 = Node('', parent = node21)
node36 = Node('8', parent = node22)
node37 = Node('3', parent = node22)
node38 = Node('', parent = node23)
node39 = Node('2', parent = node23)
node310 = Node('', parent = node23)
node311 = Node('', parent = node24)
node312 = Node('8', parent = node24)
node313 = Node('', parent = node24)
node40 = Node('5', parent = node33)
node41 = Node('2', parent = node33)
node42 = Node('8', parent = node33)
node43 = Node('0', parent = node33)
node44 = Node('5', parent = node35)
node45 = Node('7', parent = node35)
node46 = Node('1', parent = node35)
node47 = Node('3', parent = node38)
node48 = Node('6', parent = node38)
node49 = Node('4', parent = node38)
node410 = Node('9', parent = node310)
node411 = Node('3', parent = node310)
node412 = Node('0', parent = node310)
node413 = Node('8', parent = node311)
node414 = Node('1', parent = node311)
node415 = Node('9', parent = node311)
node416 = Node('3', parent = node313)
node417 = Node('4', parent = node313)

"""


"""
#the third case  
rootnode = Node('')
node10 = Node('5', parent = rootnode)
node11 = Node('', parent = rootnode)
node20 = Node('', parent = node11)
node21 = Node('6', parent = node11)
node30 = Node('', parent = node20)
node31 = Node('7', parent = node20)
node40 = Node('4', parent = node30)
node41 = Node('7', parent = node30)
node42 = Node('-2', parent = node30)

"""



"""
#the forth case
rootnode = Node('')
node10 = Node('', parent = rootnode)
node11 = Node('', parent = rootnode)
node20 = Node('8', parent = node10)
node21 = Node('', parent = node10)
node22 = Node('4', parent = node10)
node23 = Node('', parent = node11)
node24 = Node('', parent = node11)
node30 = Node('7', parent = node21)
node31 = Node('9', parent = node21)
node32 = Node('8', parent = node21)
node33 = Node('', parent = node23)
node34 = Node('2', parent = node23)
node35 = Node('1', parent = node23)
node36 = Node('', parent = node24)
node37 = Node('4', parent = node24)
node38 = Node('7', parent = node24)
node39 = Node('', parent = node24)
node40 = Node('3', parent = node33)
node41 = Node('6', parent = node33)
node42 = Node('4', parent = node33)
node43 = Node('6', parent = node36)
node44 = Node('2', parent = node36)
node45 = Node('9', parent = node36)
node46 = Node('6', parent = node39)
node47 = Node('4', parent = node39)
node48 = Node('5', parent = node39)

"""


"""
#the fifth case
rootnode = Node('')
node10 = Node('', parent = rootnode)
node11 = Node('', parent = rootnode)
node20 = Node('', parent = node10)
node21 = Node('', parent = node10)
node22 = Node('', parent = node10)
node23 = Node('', parent = node11)
node24 = Node('', parent = node11)
node30 = Node('1', parent = node20)
node31 = Node('', parent = node20)
node32 = Node('3', parent = node21)
node33 = Node('', parent = node21)
node34 = Node('7', parent = node21)
node35 = Node('', parent = node21)
node36 = Node('8', parent = node22)
node37 = Node('3', parent = node22)
node38 = Node('', parent = node23)
node39 = Node('2', parent = node23)
node310 = Node('', parent = node23)
node311 = Node('', parent = node24)
node312 = Node('8', parent = node24)
node313 = Node('', parent = node24)
node40 = Node('4', parent = node31)
node41 = Node('7', parent = node31)
node42 = Node('', parent = node33)
node43 = Node('', parent = node33)
node44 = Node('0', parent = node33)
node45 = Node('-2', parent = node33)
node46 = Node('5', parent = node35)
node47 = Node('7', parent = node35)
node48 = Node('1', parent = node35)
node49 = Node('8', parent = node38)
node410 = Node('', parent = node38)
node411 = Node('5', parent = node38)
node412 = Node('9', parent = node310)
node413 = Node('', parent = node310)
node414 = Node('0', parent = node310)
node415 = Node('3', parent = node311)
node416 = Node('1', parent = node311)
node417 = Node('9', parent = node311)
node418 = Node('3', parent = node313)
node419 = Node('4', parent = node313)
node50 = Node('5', parent = node42)
node51 = Node('2', parent = node42)
node52 = Node('2', parent = node43)
node53 = Node('8', parent = node43)
node54 = Node('9', parent = node43)
node55 = Node('9', parent = node410)
node56 = Node('3', parent = node410)
node57 = Node('2', parent = node410)
node58 = Node('3', parent = node413)
node59 = Node('2', parent = node413)

""" 



#the forth case
rootnode = Node('')
node10 = Node('', parent = rootnode)
node11 = Node('', parent = rootnode)
node20 = Node('8', parent = node10)
node21 = Node('', parent = node10)
node22 = Node('4', parent = node10)
node23 = Node('', parent = node11)
node24 = Node('', parent = node11)
node30 = Node('7', parent = node21)
node31 = Node('9', parent = node21)
node32 = Node('8', parent = node21)
node33 = Node('', parent = node23)
node34 = Node('2', parent = node23)
node35 = Node('1', parent = node23)
node36 = Node('', parent = node24)
node37 = Node('4', parent = node24)
node38 = Node('7', parent = node24)
node39 = Node('', parent = node24)
node40 = Node('3', parent = node33)
node41 = Node('6', parent = node33)
node42 = Node('4', parent = node33)
node43 = Node('6', parent = node36)
node44 = Node('2', parent = node36)
node45 = Node('9', parent = node36)
node46 = Node('6', parent = node39)
node47 = Node('4', parent = node39)
node48 = Node('5', parent = node39)

for pre, fill, node in RenderTree(rootnode):
    print("%s%s" % (pre, node.name))
  
def min_max(node, maximizingPlayer):
    if((node.depth == 0 and node.name != '' ) or node.is_leaf):
        return node.name
 
    if (maximizingPlayer == TRUE):
        bestValue = -INFINITY
        for childnode in node.children:
            v = min_max(childnode, FALSE)
            #print "max"
            #print "v is:", v, "bestValue is:", bestValue
            v_num = int(v) 
            bestValue = max(v_num,bestValue)
            #print "now bestvalue is:", bestValue
        #node.name = bestValue
        return bestValue 
    else:
        bestValue = +INFINITY
        for childnode in node.children:
            v = min_max(childnode, TRUE)
           # print "min"
           # print "v is:", v, "bestValue is:", bestValue
            v_num = int(v)
            bestValue = min(v_num,bestValue)
           # print "now bestvalue is:", bestValue
        #node.name = bestValue
        return bestValue


def alpha_beta(node, alpha, beta, maximizingPlayer):
    if((node.depth == 0 and node.name != '' ) or node.is_leaf):
        return node.name
    
    if (maximizingPlayer == TRUE):
        v = -INFINITY
        for childnode in node.children:
            temp = alpha_beta(childnode,alpha,beta,FALSE)
            v = max(alpha, int(temp))
            #print "max"
           # print "the value of childnode is:", alpha_beta(childnode,alpha,beta,FALSE)
            #print "alpha is:", alpha
            #print "v is:", v
            #print "beta is:", beta
            if v >= beta:
                print "beta cut-off"
                break
            alpha = max(v,alpha)
            #print "alpha now is:", alpha
        return v
    else:
        v = INFINITY
        for childnode in node.children:
            temp = alpha_beta(childnode,alpha,beta,TRUE)
            v = min(beta, int(temp))
            #print "min"
            #print "the value of childnode is:", alpha_beta(childnode,alpha,beta,FALSE)
            #print "beta is:", beta
            #print "v is:", v
            #print "alpha is:", alpha
            if v <= alpha:
                print "alpha cut-off"
                break
            beta = min(v,beta)
            #print "beta now is:", beta
        return v
        

# Main method
def main():
    RenderTree(rootnode)
    result1 = min_max(rootnode,TRUE)
    print "The searching result of min-max is:", result1
    node = rootnode
    while not node.is_leaf:
        for child in node.children:
            if child.name == node.name:
                print node,"->",child
                node = child
    result2 = alpha_beta(rootnode,-INFINITY,+INFINITY,TRUE)
    print "The searching result of alpha-beta is:", result2
    
  
# A python-isim. Basically if the file is being run execute the main() function.
if __name__ == "__main__":
	main()

