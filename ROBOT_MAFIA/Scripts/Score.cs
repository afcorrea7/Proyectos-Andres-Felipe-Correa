using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Score : MonoBehaviour
{
    public GameObject bulletObject;
    public Text scoreText;
    public GameObject[] spriteMultipliers;
    private Bullet bulletScript;
    private int numScore;
    private int newNumScore;
    //private Animator[] spriteAnim;

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("spriteMultipliers.Length: "+spriteMultipliers.Length);
        for(int i=0; i<spriteMultipliers.Length;i++){
            spriteMultipliers[i].SetActive(false);
            Debug.Log("i spriteM "+i);
        }

        // for(int j=0; j<spriteMultipliers.Length;j++){
        //     spriteAnim[j] = spriteMultipliers[j].GetComponent<Animator>();
        //     Debug.Log("j spriteA "+j);
        // }

        bulletScript = bulletObject.GetComponent<Bullet>();
    }

    // Update is called once per frame
    void Update(){

    }

    public IEnumerator AddBounceScore(int bCount){
        Debug.Log("bCount: "+bCount);
        Debug.Log("numScore Before while: "+numScore);
        numScore+=bCount;

        while(newNumScore<numScore){
            newNumScore+=20;
            scoreText.text = newNumScore.ToString();
            Debug.Log(newNumScore);
            yield return new WaitForSeconds(0.01f);
        }
    }

    public IEnumerator MultiplierSprite(int i){
        spriteMultipliers[i-1].SetActive(true);
        yield return new WaitForSeconds(0.6f);
        //spriteAnim[i-1].SetTrigger("Vanish");
        spriteMultipliers[i-1].SetActive(false);
    }
}

