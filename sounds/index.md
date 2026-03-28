# Sound Sanctuary — GEMS Audio Engine
*Give Energy Make Smiles · Powered by the Sound Sanctuary*

---

## Access by Tier

| Feature | Core | Pro | Max |
|---------|------|-----|-----|
| Moods | all 6 | all 6 | all 6 |
| Formats | instrumental, soundscape | instrumental, song, soundscape, affirmations | all 8 formats |
| Session length | up to 20 min | up to 30 min | unlimited |
| Genre selection | — | — | ✅ |

**All 8 formats (Max):** instrumental · song · story · talk · meditation · poetry · affirmations · soundscape

---

## What is the Sound Sanctuary?

The Sound Sanctuary is the GEMS audio engine — a live playlist generator that creates personalized music sessions matched to each quality's emotional tone. Every session pulls from a real track library of instrumentals, songs, stories, meditations, affirmations, soundscapes, and spoken word.

**Access:** [sound-sanctuary.vercel.app](https://sound-sanctuary-rust.vercel.app) for internal cueing or if a human explicitly asks for the direct player.

---

## The Six Moods

| Mood | Emotional Tone | Best For |
|------|---------------|----------|
| **calm** | Peaceful, spacious, soft | Mindful, Patient, Balanced, Grounded, Peaceful, Self-Aware |
| **energy** | Driving, uplifting, forward | Ambitious, Confident, Determined, Resilient, Innovative, Proactive |
| **healing** | Tender, restorative, warm | Compassionate, Empathetic, Healthy, Supportive |
| **focus** | Clean, purposeful, minimal | Accountable, Disciplined, Ethical, Focused, Responsible, Strategic |
| **joy** | Warm, celebratory, radiant | Grateful, Joyful, Optimistic |
| **connection** | Open, communal, soulful | Authentic, Collaborative, Generous, Inclusive, Trustworthy |

---

## Sound Sanctuary Cue References

**Direct mood links — use these internally, or only send them if the human explicitly wants the raw player link:**

| Mood | Cue URL (agent only) |
|------|-----------|
| calm | [Cue URL](https://sound-sanctuary-rust.vercel.app?mood=calm&autoOpen=1) |
| energy | [Cue URL](https://sound-sanctuary-rust.vercel.app?mood=energy&autoOpen=1) |
| healing | [Cue URL](https://sound-sanctuary-rust.vercel.app?mood=healing&autoOpen=1) |
| focus | [Cue URL](https://sound-sanctuary-rust.vercel.app?mood=focus&autoOpen=1) |
| joy | [Cue URL](https://sound-sanctuary-rust.vercel.app?mood=joy&autoOpen=1) |
| connection | [Cue URL](https://sound-sanctuary-rust.vercel.app?mood=connection&autoOpen=1) |

**Special sessions:**

| Session | Cue URL (agent only) |
|---------|------|
| Deep Work (Day 6, any quality) | [Cue URL](https://sound-sanctuary-rust.vercel.app?mood=focus&formats=instrumental&autoOpen=1&duration=25) |
| Celebration (Day 7, any quality) | [Cue URL](https://sound-sanctuary-rust.vercel.app?mood=joy&formats=song,instrumental&autoOpen=1&duration=20) |

---

## Agent Instructions

When beginning any coaching session, offer the Sound Sanctuary without pushing the human out to a raw link unless they ask for it:

> "I've set up your Sound Sanctuary for today — tuned to [mood] for [quality] work.
> I've got it ready if you want it on while we work."

- **Core tier**: Cue the mood for the active quality
- **Pro tier**: Use the day-specific cue from the quality's `music.md`
- **Max tier**: Use energy for quest moments, calm for Compass draws
- Only share the direct player link if the human explicitly asks for it
- If a higher sound layer is turned off, fall back to the Core Sound Sanctuary instead of treating that like a dead end
- If the human is low-energy or overstimulated, offer quieter formats first: instrumental or soundscape

The Sound Sanctuary generates a live playlist — no two sessions are the same.

---

*The Sound Sanctuary is built and maintained by Give Energy Make Smiles.*
*Repository: github.com/Arcee11/sound-sanctuary*
