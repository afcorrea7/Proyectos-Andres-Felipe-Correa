using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CrateScript : MonoBehaviour
{
    public float shakeAmount = 0.07f;
    public int health = 5;

    public AudioClip[] crateSounds;
    public Object destructableRef;

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
        if(isShaking == true)
        {
            transform.position = startPos + UnityEngine.Random.insideUnitCircle * shakeAmount;
        }

        if (health <= 0)
        {
            Invoke("StopShaking", 0.01f);
            ExplodeCrate();
        }
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
       if(other.gameObject.tag == "Punch")
        {
            isShaking = true;
            aud.clip = crateSounds[Random.Range(0, crateSounds.Length)];
            aud.PlayOneShot(aud.clip);
            health -= 1;

            Invoke("StopShaking", 0.5f);
        } 

       if(other.gameObject.tag == "Fireball")
        {
            isShaking = true;
            aud.clip = crateSounds[Random.Range(0, crateSounds.Length)];
            aud.PlayOneShot(aud.clip);
            health -= 5;

            Invoke("StopeShaking", 0.5f);
        }
    }

    void StopShaking()
    {
        isShaking = false;
        transform.position = startPos;
    }

    void ExplodeCrate()
    {
        GameObject destructable = (GameObject)Instantiate(destructableRef);

        //map the loaded destructable object to the x and y position of the destroyed Crate
        destructable.transform.position = transform.position;

        Destroy(gameObject);
    }
}
