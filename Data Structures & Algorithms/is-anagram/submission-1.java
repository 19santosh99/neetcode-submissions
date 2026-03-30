class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> map = new HashMap();
        HashMap<Character, Integer> map1 = new HashMap();
        for (Character c: s.toCharArray()) {
            if(map.containsKey(c)){
                map.put(c, map.get(c) + 1 );
            } else {
                map.put(c, 1);
            }
            
        }

        for (Character c: t.toCharArray()) {
            if(map1.containsKey(c)){
                map1.put(c, map1.get(c) + 1 );
            } else {
                map1.put(c, 1);
            }
        }

        for(Character c : s.toCharArray()) {
            if(!(map.get(c) == map1.get(c))){
                return false;
            }
        }

        return true;
    }
}
