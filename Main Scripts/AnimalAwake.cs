using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimalAwake : MonoBehaviour
{
    private GameObject source;
    private AudioSource audiosrc;
    private bool ready = false;
    private AudioClip clip;

    void Start()
    {
        source = GameObject.FindGameObjectWithTag("MasterSound");
        audiosrc = source.GetComponent<AudioSource>();
        clip = (AudioClip)Resources.Load("Sounds/Boing");
    }

    void Update()
    {
        ReadyCheck();
    }

    void ReadyCheck(){
        if (ready == true)
        {
            audiosrc.PlayOneShot(clip);
            ready = false;
        }
    }

    void OnEnable()
    {
        Debug.Log("Animal on OnEnable()");
        ready = true;
    }

}
