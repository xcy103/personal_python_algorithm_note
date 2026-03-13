#include<bits/stdc++.h>
using namespace std;

const double sml = 1e-7;

bool gauss(vector<vector<double>>mat,int n){
    for(int i=0;i<n;i++){
        int max_row = i;
        
        for(int j=i+1;j<n;j++){
            if(fabs(mat[j][i])>fabs(mat[max_row][i])){
                max_row = j;
            }
        }
        swap(mat[i],mat[max_row]);

        if(fabs(mat[i][i])<sml) return false;

        double pivot = mat[i][i];
        for(int j=i;j<n+1;j++){
            mat[i][j] /= pivot; 
        } 

        for(int j=0;j<n;j++){
            if(j==i) continue;
            double factor = mat[j][i];
            for(int k=i;k<n+1;k++){
                mat[j][k] -= factor*mat[i][k];
            }
        }
    }
    return true;
}