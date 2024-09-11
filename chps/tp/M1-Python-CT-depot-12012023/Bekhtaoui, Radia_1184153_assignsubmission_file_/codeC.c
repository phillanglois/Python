#include <stdio.h>
#include <stdlib.h>

#define N  5 

//Fonction pour afficher la grille
void print_grille(int **a,int n) {
  int i,j;

  for(i=0;i<n;i++) {
    for(j=0;j<n;j++) {
        if(a[i][j]==1) printf("x \t");
        else printf(".\t");
    }
    printf("\n");
  }
}
//ceci ne marche pas correctement 
int cmp_nb_voisins(int **a, int x, int y) {
    int count = 0;
    for (int i = x-1; i <= x+1; i++) {
        for (int j = y-1; j <= y+1; j++) {
            if (i == x && j == y) continue; // ignore la cellule elle-même
            if (i >= 0 && i < N && j >= 0 && j < N && a[i][j] == 1) {
                count++;
            }
        }
    }
    return count;
}

//Fonction pour mettre à jour l'état des cellules
void update_grille(int **a,int n){
    int i,j;
    int nb_voisins=0;

    for(i=0;i<n;i++) {
        for(j=0;j<n;j++) {
        //compter le nombre de voisins vivants
        nb_voisins = cmp_nb_voisins(a,i,j);
        }
        //mise à jour de l'état de la cellule en fonction des règles du jeu de la vie
        if (a[i][j] == 1)//si elle est vivante
            if (nb_voisins < 2 || nb_voisins > 3)
                a[i][j] = 0; // maj à 0 : elle meurt 
            else if (nb_voisins == 3)//si elle est morte et les voisins vivants =3
                a[i][j] = 1; //maj à 1 elle devient vivante (elle naît) 
    }
    
}
int main(){
    int **grille;
    int i;

    grille = (int**)malloc(N*sizeof(int*));
   
    for(i=0;i<N;i++) {
            grille[i] = (int*)malloc(N*sizeof(int));
    }
    //ici lire fichier ================================================
    //initialisation de la grille exemple sujet
   
    grille[2][1] = 1;
    grille[2][2] = 1;
    grille[2][3] = 1;
    printf("grille nitiale :\n");
    print_grille(grille,N);
    printf("\n");
    
    //Répéter ce traitement pour un nombre d’itérations fixé ici à 4 par exemple :
    for (i=0;i<4;i++){
        update_grille(grille,N);
        printf("grille :%d\n",i+1 );
        print_grille(grille,N);
        printf("\n");
    }
    //répéter ce traitement selon la lecture d’un caractère au clavier : la lettre F met fin à la simulation.
    /*printf("#=========Bienvenue dans le jeu de la vie !!! =========#\n")
    printf("grille nitiale : \n")
    print_grille(grille)
    char stop = "c";
    while(stop != "F" ){
        stop=input("Pour arreter le jeu tapez \"F\"! Pour continuner tapez autres!" )
        grille = update_grille(grille)
        print("grille",i+1 ,":")
        print_grille(grille)
        print("\n")
        }
        manque de tzemps 
    */

}
    