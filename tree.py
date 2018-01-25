# -*- coding: utf-8 -*-
# Copyright 2018 cn_fgzhang
#
# 树和二叉树数据结构
# 通过前缀表达式构建树或二叉树
# a copy of the License at
#
#     https://github.com/angrySmeagol/data-structure-and-algorithm-python
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


class Tree(object):

    def __init__(self):
        self.data = None
        self.children = []

    def polish(self):
        data = ""
        data += self.data
        for i in self.children:
            if not i:
                data += '$'
            else:
                data += i.polish()
        return data

    def destroy(self):
        pass

    def create(self):
        pass

    def clear(self):
        pass

    def is_empty(self):
        pass

    def depth(self):
        pass

    def root(self):
        pass

    def value(self, e):
        pass

    def assign(self, e, value):
        pass

    def parent(self, e):
        pass

    def left_child(self, e):
        if self.data == e:
            return self.children[0]
        else:
            for i in self.children:
                if i is None:
                    return False
                result = i.left_child(e)
                if result is not False:
                    return result
            return False

    def right_sibling(self, e):
        pass

    def insert_child(self, e, i, c):
        pass

    def delete_child(self, e, i):
        pass

    def traverse_tree(self, fuc):
        pass


class BiTree(Tree):

    def __init__(self):
        super(BiTree, self).__init__()
        self.data = None
        self.l_child = None
        self.r_child = None

    def left_child(self, e):
        if self.data == e:
            return self.l_child
        else:
            if not self.l_child:
                return False
            result = self.l_child.left_child(e)
            if result is not False:
                return result
            if not self.r_child:
                return False
            result = self.r_child.left_child(e)
            if result is not False:
                return result
            return False

    def right_child(self, e):
        if self.data == e:
            return self.r_child
        else:
            if not self.l_child:
                return False
            result = self.l_child.right_child(e)
            if result is not False:
                return result
            if not self.r_child:
                return False
            result = self.r_child.right_child(e)
            if result is not False:
                return result
            return False

    def left_sibling(self, e):
        pass

    def insert_child(self, e, lr, c):
        pass

    def delete_child(self, e, lr):
        pass

    def pre_order_traverse(self, fuc):
        pass

    def polish(self):
        data = ""
        data += self.data
        if self.l_child:
            data += self.l_child.polish()
        else:
            data += "$"
        if self.r_child:
            data += self.r_child.polish()
        else:
            data += "$"
        return data

    def in_order_traverse(self, fuc):
        pass

    def post_order_traverse(self, fuc):
        pass

    def leave_order_traverse(self, fuc):
        pass


class CreateBiTree(object):
    def __init__(self, pre_expression):

        self.data = list(pre_expression)

    def create_bi_tree(self):
        # 波兰式 pre_expression = "234$$$15$$$"

        temp, self.data = self.data[0], self.data[1:]
        if temp == '$':
            return None
        b = BiTree()
        b.data = temp
        b.l_child = self.create_bi_tree()
        b.r_child = self.create_bi_tree()
        return b


class CreateTree(object):
    def __init__(self, pre_expression):
        self.data = list(pre_expression)

    def create_tree(self):
        # polish pre_expression = "1256$$$378$$$49ac$d$e$f$$b$$$$"

        temp, self.data = self.data[0], self.data[1:]
        if temp == "$":
            return None
        b = Tree()
        b.data = temp
        flag = True
        while flag:
            c = self.create_tree()
            if not c:
                flag = False
            b.children.append(c)
        return b
