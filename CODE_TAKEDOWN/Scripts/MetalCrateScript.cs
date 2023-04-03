using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MetalCrateScript : MonoBehaviour
{
    public float shakeAmount = 0.07f;
    public AudioClip metalHit;

    private bool isShaking;

    Vector2 startPos;

    AudioSource aud;
    // Start is called before the first frame update
    void Start()
    {
        aud = GetComponent<AudioSource>();
        startPos = transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        if (isShaking == true)
        {
            transform.position = startPos + UnityEngine.Random.insideUnitCircle * shakeAmount;
        }
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.gameObject.tag == "Punch" || other.gameObject.tag == "Fireball")
        {
            isShaking = true;
            aud.PlayOneShot(metalHit);
            Invoke("StopShaking", 0.5f);
        }
    }

    void StopShaking()
    {
        isShaking = false;
        transform.position = startPos;
    }
}
