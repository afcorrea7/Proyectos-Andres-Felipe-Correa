using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SoundOnAwake : MonoBehaviour
{
    public AudioClip crateBrake;

    AudioSource aud;
    // Start is called before the first frame update
    void Start()
    {
        aud = GetComponent<AudioSource>();

        aud.PlayOneShot(crateBrake);
    }
}
