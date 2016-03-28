#!/usr/bin/python
#-*-coding:utf-8-*-

class TreeNode(object):              #用作根节点
    def __init__(self,left=0,right=0,data=0):   #初始化节点
        self.left=left
        self.right=right
        self.data=data

class binary_Tree(object):          #用作生成树
    def __init__(self,root,mark=0):        #初始化生成树
        self.root=root
        self.mark=mark
        
    def is_empty(self):             #判断节点是否为空
        if self.root==0:
            return True
        else:
            return False
    
    def create(self,treenode):        #用递归的方法生成二叉树
        temp=input('Please enter a value')          #输入一个节点的数据值
        if temp==99:             #如果输入99则说明是空的，返回0
            if treenode.data!=0:
                if treenode.left==0:
                    if self.mark==0:
                        self.mark=1
                    else:
                        self.mark=0
            return 0
        treenode1=TreeNode()   #否则，根据输入的temp生成一个节点
        treenode1.data=temp
        if self.root.data==0:               #将生成的节点加到树里面
            self.root=treenode1
        elif treenode.left==0:
            if self.mark==0:
                treenode.left=treenode1
            else:
                treenode.right=treenode1
                self.mark=0 
        else:
            treenode.right=treenode1
            self.mark=0
        treenode1.left=self.create(treenode1)     #递归产生左边的树
        treenode1.right=self.create(treenode1)    #递归产生右边的树
        return treenode1                          #返回头结点
    
    def pre_order(self,treenode):                 #前序遍历
        if treenode==0:
            return
        print treenode.data
        self.pre_order(treenode.left)
        self.pre_order(treenode.right)
        
    def in_order(self,treenode):                  #中序遍历
        if treenode==0:
            return
        self.in_order(treenode.left)
        print treenode.data
        self.in_order(treenode.right)
        
    def post_order(self,treenode):                 #后序遍历
        if treenode==0:
            return
        self.post_order(treenode.left)
        self.post_order(treenode.right)
        print treenode.data
    
treenode=TreeNode()
kengkeng=binary_Tree(treenode)
kk=kengkeng.create(treenode)
if kengkeng.is_empty()==True:
    print 'It is empty'
else:
    print 'Pre order traversal results:'
    kengkeng.pre_order(kk)
    print 'Traversal results in order:'
    kengkeng.in_order(kk)
    print 'After traversal results:'
    kengkeng.post_order(kk)


        
            
        

