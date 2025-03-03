// start at 2:40

class Node {
    constructor(num, x, y){
        this.num = num;
        this.x = x;
        this.y = y;
        this.leftChild = null;
        this.rightChild = null;
    }
}

class Tree {
    constructor() {
        this.root = null;
    }
    push(node){
        if (this.root == null) {
            this.root = node
            return;
        }
        let root = this.root;
        this.find_position(root, node);
    }
    find_position(root, node){
        if (root.x < node.x) {
            if (root.rightChild == null) {
                root.rightChild = node;
                return ;
            }
            this.find_position(root.rightChild, node);
        }
        else {
            if (root.leftChild == null) {
                root.leftChild = node;
                return ;
            }
            this.find_position(root.leftChild, node);
        }
    }
}

function solution(nodeinfo) {

    for (let i = 0; i < nodeinfo.length; i++){
        nodeinfo[i].push(i + 1);
    }

    nodeinfo.sort((a, b) => b[1] - a[1]);
    const tree = new Tree();

    for (const [x, y, num] of nodeinfo) {
        const node = new Node(num, x, y);
        tree.push(node);
    }

    const preArr = [];
    const postArr = [];
    function preorder(root){
        preArr.push(root.num);
        if (root.leftChild) preorder(root.leftChild);
        if (root.rightChild) preorder(root.rightChild);
    }
    
    function postorder(root){
        if (root.leftChild) postorder(root.leftChild);
        if (root.rightChild) postorder(root.rightChild);
        postArr.push(root.num);
    }

    preorder(tree.root);
    postorder(tree.root);

    return [preArr, postArr];
}

const nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]];
console.log(solution(nodeinfo));