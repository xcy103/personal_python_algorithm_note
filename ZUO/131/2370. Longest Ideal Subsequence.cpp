class Solution {
public:
    static const int MAXN = 27;
    int max_tree[MAXN<<2];
    int n;

    
    int longestIdealString(string s, int k) {
        n = s.size();
        int ans = 0;
        for(int i=0;i<n;i++){
            char ch = s[i];
            int val = query(max(1,ch-'a'-k+1),min(26,ch-'a'+k+1),1,26,1);
            update(ch-'a'+1,val+1,1,26,1);
            ans = max(ans,val+1);
        }
        return ans;
    }

    void up(int i){
        max_tree[i] = max(max_tree[i<<1],max_tree[i<<1|1]);
    }
    void build(int l,int r,int i){
        if(l==r){
            max_tree[i] = 0;
        }else{
            int mid = (l+r)>>1;
            build(l,mid,i<<1);
            build(mid+1,r,i<<1|1);
            up(i);
        }
    }
    void update(int jobi,int jobv,int l,int r,int i){
        if(l==r){
            max_tree[i] = jobv;
        }else{
            int mid = (l+r)>>1;
            if(jobi<=mid){
                update(jobi,jobv,l,mid,i<<1);
            }else{
                update(jobi,jobv,mid+1,r,i<<1|1);
            }
            up(i);
        }
    }
    int query(int jobl, int jobr, int l, int r, int i){
        if(jobl<=l&&r<=jobr){
            return max_tree[i];
        }
        int mid = (l+r)>>1;
        int ans = 0;
        if(jobl<=mid){
            ans = max(ans,query(jobl,jobr,l,mid,i<<1));
        }
        if(jobr>mid){
            ans = max(ans,query(jobl,jobr,mid+1,r,i<<1|1));
        }
        return ans;
    }
};