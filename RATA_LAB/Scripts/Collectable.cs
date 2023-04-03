/*
    Rata Lab - Andrés Felipe Correa
    2023
*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class Collectable : MonoBehaviour
{
    WinState winScript;
    public AudioSource audioCollectable;
    public GameObject eatParticles;
    public int cheeseWorth = 1;

    void Start(){
        winScript = FindObjectOfType<WinState>(); //Find Win Condition Script, so we can update the UI
    }

    void OnTriggerEnter(Collider other){
        if(other.tag=="Player"){
            Debug.Log("CHEESE MADE CONTACT WITH THE RAT");
            audioCollectable.Play();
            winScript.CountUp(cheeseWorth);
            Instantiate(eatParticles, this.gameObject.transform);
            //The cheese has been eaten, so we destroy the mesh that was a child and later the particles, finally the parent itself is destroyed
            DestroySequence();
        }
    }

    void DestroySequence(){//The cheese game object'll only ever have two children
        Destroy(GetComponent<BoxCollider>()); //Destroy the collider first so that the player doesn't collect the cheese more than once
        Destroy(transform.GetChild(0).gameObject, 0.1f); //The cheese mesh will always be child number 0
        Destroy(transform.GetChild(1).gameObject, 2); //The cheese particles will always be child number 1
        Destroy(gameObject, 2); //Destroy the cheese itself
    }
}
