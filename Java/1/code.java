public class BouncingBall {
	
	public static int bouncingBall(double h, double bounce, double window) {
    if (h > 0 && 0 < bounce && bounce < 1 && window < h){
        int res = 1;
        h *= bounce;
        while (h > window){
            res += 2;
            h *= bounce;
        }
        return res;
    }
    return -1;
	}
}
