using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PanelAwake : MonoBehaviour
{
    private GameObject source;
    private AudioSource audiosrc;
    private bool ready = false;
    private AudioClip clip;

    // Start is called before the first frame update
    void Start()
    {
        source = GameObject.FindGameObjectWithTag("MasterSound");
        audiosrc = source.GetComponent<AudioSource>();
        clip = (AudioClip)Resources.Load("Sounds/CardFlip");
    }

    // Update is called once per frame
    void Update()
    {
        if (ready == true)
        {
            audiosrc.PlayOneShot(clip);
            ready = false;
        }
    }

    void OnEnable()
    {
        Debug.Log("Panel on OnEnable()");
        ready = true;
    }

}
