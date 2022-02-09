using System;

namespace Random_sentance
{
    class Program
    {
        static void Main(string[] args)
        {
            long num;
            int seed;
            string ans, text="";
            int x=0, y=0, z=0, osszeg = 0;
            int begining=0, previous=0;
            char[] letter = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' };
            /*12+, prev:0*/string[] w_thing = { " car", " cat", " ice cream", " building", " house", " freezer", " doll", " art", " computer", " code", " table", " chair", " mouse", " keyboard", " monitor", " processor", " ram", " fruit", " vegetable", " desk", " pen", " pencil", " gun", " death", " paint", " brush", /**/};
            /*8+, prev:1*/string[] w_do = { " eat", " give", " take", " do", " make", " destroy", " code", " can", " slap", " kick", " leave", " go", " morn", " capture", " run", " walk", " jog", " climb", /**/};
            /*DONE 12 , prev:2*/string[] w_who = { " I", " you", " he", " she", " it", " they", " them", " her", " his", " me", " this", " that" };
            /*DONE 7 , prev:3*/string[] w_ask = { "who", "when", "why", "where", "what", "are", "is" };
            /*DONE 8 */string[] w_end = { ".", "!", "?", "?!", "!?", " :)", "", "...", };
            /*DONE 9 , prev:4*/string[] w_between = { " a", " an", " is", " the", " with", " at", " on", " in", " are"};
            //random number
            Random rs = new Random();
            seed = rs.Next(-2147483648, 2147483647);
            Console.Write("Seed? :");
            ans = Console.ReadLine();
            if (ans != "")
            {
                try
                {
                    seed = Convert.ToInt32(ans);
                }
                catch
                {
                    for (x = 0; x < ans.Length; x++)
                    {
                        osszeg += (int)ans[x];
                    }
                    seed = osszeg;
                }
            }
            Random r = new Random(seed);
            num = r.Next(1, 2147483647);
            Console.WriteLine("SEED:" + seed);
            Console.WriteLine(num + ", \n");
            //random text?
            Console.Write("Rndom? :");
            ans = Console.ReadLine();
            //very random
            if(ans=="y")
            {
                num = r.Next(1, 1001);
                for(x=0;x<num;x++)
                {
                    y = r.Next(0, 60);
                    text += letter[y];
                }
            }






            //not so random
            else
            {
                //begining word
                num = r.Next(0, 4);
                if(num==1)
                {
                    y = r.Next(0, w_ask.Length-1);
                    text += w_ask[y];
                    if (y == 5 && y == 6)
                    {
                        y = r.Next(0, w_who.Length-1);
                        text += w_who[y];
                        previous = 2;
                    }
                    else
                        begining = 3;
                }
                else if(num==2)
                {
                    y = r.Next(0, w_ask.Length-1);
                    text += w_ask[y];
                    if (y == 5 || y == 6)
                    {
                        y = r.Next(0, w_who.Length-1);
                        text += w_who[y];
                        previous = 2;
                    }
                    else
                        begining = 3;
                }
                else if(num==3)
                {
                    y = r.Next(0, w_who.Length-1);
                    text += w_who[y];
                    begining = 2;
                    previous = 2;
                }
                else if (num == 4)
                {
                    y = r.Next(0, w_do.Length-1);
                    text += w_do[y];
                    begining = 1;
                    previous = 1;
                }
                //sentance
                /*
                 *thing=0
                 *do=1
                 *who=2
                 *ask=3
                 *between=4
                 *
                 *STRUCTURE:
                 *thing-between
                 *do-thing
                 *do-between
                 *who-do
                 *who-between
                 *ask-who
                 *ask-between
                 *between-who
                 *between-thing
                */
                if (num > 1)
                {
                    num = r.Next(1, 101);
                    for (x = 0; x < num; x++)
                    {
                        if(previous==0)
                        {
                            y = r.Next(0, 0);
                            if (y == 0)
                            {
                                z = r.Next(0, w_between.Length - 1);
                                text += w_between[z];
                                previous = 4;
                            }
                        }
                        else if (previous == 1)
                        {
                            y = r.Next(0, 2);
                            if (y == 0)
                            {
                                z = r.Next(0, w_between.Length - 1);
                                text += w_between[z];
                                previous = 4;
                            }
                            else
                            {
                                z = r.Next(0, w_thing.Length - 1);
                                text += w_thing[z];
                                previous = 0;
                            }
                        }
                        else if (previous == 2)
                        {
                            y = r.Next(0, 2);
                            if (y == 0)
                            {
                                z = r.Next(0, w_between.Length - 1);
                                text += w_between[z];
                                previous = 4;
                            }
                            else
                            {
                                z = r.Next(0, w_do.Length - 1);
                                text += w_do[z];
                                previous = 1;
                            }
                        }
                        else if (previous==3)
                        {
                            y = r.Next(0, 2);
                            if (y == 0)
                            {
                                z = r.Next(0, w_between.Length - 1);
                                text += w_between[z];
                                previous = 4;
                            }
                            else
                            {
                                z = r.Next(0, w_who.Length - 1);
                                text += w_who[z];
                                previous = 2;
                            }
                        }
                        else
                        {
                            y = r.Next(0, 1);
                            if (y == 0)
                            {
                                z = r.Next(0, w_who.Length - 1);
                                text += w_who[z];
                                previous = 2;
                            }
                            else
                            {
                                z = r.Next(0, w_thing.Length - 1);
                                text += w_thing[z];
                                previous = 0;
                            }
                        }
                    }
                }
                //end
                num = r.Next(0, w_end.Length-1);
                text += w_end[num];
            }
            Console.WriteLine(text);
            Console.ReadKey();
        }
    }
}
