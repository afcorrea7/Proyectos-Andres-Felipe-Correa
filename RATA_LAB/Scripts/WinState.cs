/*
    Rata Lab - Andrés Felipe Correa
    2023
*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class WinState : MonoBehaviour
{
    MoveCamera moveCamera;
    public TextMeshProUGUI counterText;
    public Image winScreen;
    public TextMeshProUGUI timerText;
    public float timeAmount = 90f;
    public Image loseScreen;
    public int winCount=10;
    public int uiCheeseCounter=0;

    private bool canLose = true;

    void Start(){
        winScreen.gameObject.SetActive(false);
        UpdateCounter();
        moveCamera = FindObjectOfType<MoveCamera>();
    }

    void Update()
    {
        if (timeAmount > 0){
            timeAmount -= Time.deltaTime;
        }else{
            timeAmount = 30000; //Set time to an exaggerated amount so LoseCall is only called once
            LoseCall();
        }

        TimerDecrease(timeAmount);
    }

    public void TimerDecrease(float timeAmount){
        if(timeAmount < 0){
            timeAmount = 0;
        }

        float minutes = Mathf.FloorToInt(timeAmount / 60);
        float seconds = Mathf.FloorToInt(timeAmount % 60);

        timerText.text = string.Format("{0:00}:{1:00}", minutes, seconds);
    }
    
    public void CountUp(int cheese){ //Cheese usually counts as 1 point, value can be changed in Collectable.cs
        uiCheeseCounter += cheese;
        Debug.Log("Collectables: "+uiCheeseCounter);
        UpdateCounter();
    }

    void UpdateCounter(){
        counterText.text = "Quesos: "+uiCheeseCounter.ToString()+"/"+winCount.ToString(); //i.e: Quesos: 5/10
        if(uiCheeseCounter==winCount){
                WinCall();
            }
    }

    void HideUI()
    {
        counterText.gameObject.SetActive(false);
        timerText.gameObject.SetActive(false);
    }

    void WinCall()
    {
        canLose = false;
        HideUI();
        winScreen.gameObject.SetActive(true);
        moveCamera.WinState(); //access MoveCamera.cs method
    }

    void LoseCall()
    {   
        if(canLose){
            HideUI();
            loseScreen.gameObject.SetActive(true);
            moveCamera.LoseState();
        }
    }
}
