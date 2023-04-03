/*
    Rata Lab - Andrés Felipe Correa
    2023
*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveCamera : MonoBehaviour
{
    public AudioClip bgClip;
    [Range(0.0f, 1.0f)]
    public float bgMusicVolumeSlider;
    public AudioClip loseClip;
    public AudioClip winClip;
    [Range(0.0f, 1.0f)]
    public float winLoseConditionVolumeSlider;

    public Transform cameraTarget;
    public Transform lookTarget;
    public float smoothSpeed = 10.0f; 
    public Vector3 distance;
    private AudioSource bgMusic;

    void Start()
    {
        bgMusic = this.gameObject.GetComponent<AudioSource>();
        bgMusic.loop = true;
        bgMusic.clip = bgClip;
        bgMusic.volume = bgMusicVolumeSlider;
        bgMusic.Play();
    }


    void FixedUpdate() {
        Vector3 dPos = cameraTarget.position + distance;
        Vector3 sPos = Vector3.Lerp(transform.position, dPos, smoothSpeed * Time.deltaTime);
        transform.position = sPos;
        transform.LookAt(lookTarget.position);

    }

    public void WinState() //Set public so Collectable.cs can access it
    {
        bgMusic.Stop();
        bgMusic.clip = winClip;
        bgMusic.loop = false;
        bgMusic.volume = winLoseConditionVolumeSlider;
        bgMusic.Play();
        
    }

    public void LoseState()
    {
        bgMusic.Stop();
        bgMusic.loop = false;
        bgMusic.clip = loseClip;
        bgMusic.volume = winLoseConditionVolumeSlider;
        bgMusic.Play();
    }
}
