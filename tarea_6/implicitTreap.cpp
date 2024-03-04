// https://habr.com/en/articles/102364/
// https://cp-algorithms.com/data_structures/treap.html
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

typedef struct item * pitem;
struct item {
    int prior, value, cnt;
    bool rev;
    pitem l, r;
};

int cnt (pitem it) {
    return it ? it->cnt : 0;
}

void upd_cnt (pitem it) {
    if (it)
        it->cnt = cnt(it->l) + cnt(it->r) + 1;
}

void push (pitem it) {
    if (it && it->rev) {
        it->rev = false;
        swap (it->l, it->r);
        if (it->l)  it->l->rev ^= true;
        if (it->r)  it->r->rev ^= true;
    }
}

void merge (pitem & t, pitem l, pitem r) {
    push (l);
    push (r);
    if (!l || !r)
        t = l ? l : r;
    else if (l->prior > r->prior)
        merge (l->r, l->r, r),  t = l;
    else
        merge (r->l, l, r->l),  t = r;
    upd_cnt (t);
}

void split (pitem t, pitem & l, pitem & r, int key, int add = 0) {
    if (!t)
        return void( l = r = 0 );
    push (t);
    int cur_key = add + cnt(t->l);
    if (key <= cur_key)
        split (t->l, l, t->l, key, add),  r = t;
    else
        split (t->r, t->r, r, key, add + 1 + cnt(t->l)),  l = t;
    upd_cnt (t);
}

void reverse (pitem t, int l, int r) {
    pitem t1, t2, t3;
    split (t, t1, t2, l);
    split (t2, t2, t3, r-l+1);
    t2->rev ^= true;
    merge (t, t1, t2);
    merge (t, t, t3);
}

void output (pitem t) {
    if (!t)  return;
    push (t);
    output (t->l);
    printf ("%d ", t->value);
    output (t->r);
}


int main() {
    vector<int> A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    vector<pair<int, int>> vecPair;

    // Add elements to the vector
    vecPair.push_back(make_pair(2, 5));
    vecPair.push_back(make_pair(4, 7));
    vecPair.push_back(make_pair(1, 9));
    
    item* T = new item();
    for (int i = 0; i < A.size(); i++) {
        if (i == 0) {
            T = new item();
            T->value = A[i];
            T->prior = rand();
            T->cnt = 1;
            T->rev = false;
            T->l = T->r = NULL;
        } else {
            pitem it = new item();
            it->value = A[i];
            it->prior = rand();
            it->cnt = 1;
            it->rev = false;
            it->l = it->r = NULL;
            merge(T, T, it);
        }
    }

    for (int i = 0; i < vecPair.size(); i++) {
        int a = vecPair[i].first;
        int b = vecPair[i].second;

        // Divide el treap en 3 partes
        // left: nodos que estan a la izquierda de a
        // middle: nodos que estan entre a y b (inclusive)
        // right: nodos que estan a la derecha de b
        pitem left, middle, right;
        split(T, left, middle, a - 1);

        split(middle, middle, right, b - a + 1);

        // Realiza el intercambio de los nodos que estan en el extremo izquierdo y derecho de la parte media
        pitem newMiddleLeft, newMiddleRight, newMiddle;

        // newMiddleLeft: nodos que estan a la izquierda del extremo derecho de middle
        // newMiddleRight: contiene el nodo del extremo derecho de middle
        split(middle, newMiddleLeft, newMiddleRight, cnt(middle) - 1);

        // Fusiona el nodo del extremo derecho de middle con left
        merge(T, left, newMiddleRight);


        // newMiddleLeft: contiene el nodo del extremo izquierdo de middle
        // newMiddleRight: nodos que estan a la derecha del extremo izquierdo de middle
        split(newMiddleLeft, newMiddleLeft, newMiddleRight, 1);

        // Fusiona T que esta ahora solo tiene los nodos del extremo izquierdo de a y el nodo
        // del extremo derecho de middle con los nodos que estan a la derecha del extremo
        // izquierdo de middle
        merge(T, T, newMiddleRight);

        // Fusiona T con con el nodo del extremo izquierdo de middle
        merge(T, T, newMiddleLeft);

        // Fusiona T con los nodos que estan a la derecha de b
        merge(T, T, right);

        cout << "T" << endl;
        output(T);
        cout << endl;
        
    }
    return 0;
}