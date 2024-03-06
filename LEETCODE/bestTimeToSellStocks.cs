// これからコメントをします。
//　いつストックを打ったら一番お金を儲けるかーと言う問題
public class Solution {
    public int MaxProfit(int[] prices) {
        //　最初にミニマムとプロフィットを決め付ける
        int min = int.MaxValue;
        int maxProfit = 0;
        //ループ
        for (int i = 0; i < prices.Length; i++){
            // 値段が一番安い値段だったら
            if (prices[i] < min) min = prices[i];
            // 今の値段が一番プロフィットしてたら
            else if (prices[i] - min > maxProfit) maxProfit = (prices[i] - min);
        }
        return maxProfit;
    }
}