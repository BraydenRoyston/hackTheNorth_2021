<template>
    <div class="how">
        <div class="root">
            <div class="title">How does it work?</div>
            <div class="body">
                <div class="section">
                    <p id="subtitle">Inspiration</p>
                    <p class="para">
                        &nbsp; &nbsp; &nbsp; &nbsp;What makes music sound good? Music theory typically discusses how different melodies, harmonies, timbres, and textures become pleasant to the human ear. However, many music lovers, particularly Hip-Hop heads, care a great deal about the lyrics and poetry behind songs. Lyricalculus aims to give an objective judging of your favorite rappers, songwriters, and emcees solely based on the quality of their lyrics. By using lexicographic, semantic, and repetition analysis, the application is able to determine with a >90% accuracy if the song is  lyrically lit  or not.
                    </p>
                </div>
                <div class="section">
                    <p id="subtitle">What it Does</p>
                    <div class="para">
                        &nbsp; &nbsp; &nbsp; &nbsp;Lyricalculus allows users to copy-paste and inject song lyrics from their favorite artists into the "Hip-Hop Robot" - a master music theorist powered by scikit-learn and NLP pre-processing. The robot compares rhymes, semantic references, and repeting themes in the song with a set of thousands of curated training examples. From this analysis, the robot returns a score out of 10 and an information breakdown of how the user's song of choice compares against the industry's best.
                    </div>
                </div>
                <div class="section">
                    <p id="subtitle">How we Built It</p>
                    <div class="para-wrapper">
                        <div class="para">
                            &nbsp; &nbsp; &nbsp; &nbsp;First, we used <a href="https://github.com/johnwmillr/LyricsGenius">johnwmillr's LyricsGenius API Wrapper</a> (an API wrapper for Genius, the popular music analysis website) to webscrape our favorite Hip-Hop music. We used music critic Iain the Great's <a href="https://iainthegreat.wordpress.com/2020/01/11/top-1000-hip-hop-and-rap-songs/" target="_blank">list of best hip hop lyrics</a> and Power 106 Radio's <a href="https://www.nme.com/news/music/new-list-of-the-top-50-worst-rappers-has-gone-viral-2559852" target="_blank">list of worst rap songs</a> as a starting point for the Hip-Hop Robot's training data. After preprocessing the data for repetition, semantic, and lexicographic analysis, we aggregated this binary training data on our MongoDB instance.
                        </div>
                        <div class="para">
                            &nbsp; &nbsp; &nbsp; &nbsp;For repetition analysis, we generated <a href="https://en.wikipedia.org/wiki/Tf%E2%80%93idf">TF-IDF scores</a> for each line in a song before using a weighted average to give it a "curated repetition score". For example, a song like <a href="https://www.youtube.com/watch?v=4LfJnj66HVQ">Lil Pump's Gucci Gang</a> would have a very high repetition score (which is bad).
                        </div>
                        <div class="para">
                            &nbsp; &nbsp; &nbsp; &nbsp;To assess semantic similarity, we used <a href="https://en.wikipedia.org/wiki/GloVe_(machine_learning)">GloVe</a> on different phrase endings in the song, which would give a semantic distance score that determines how the artist creatively connect parts of each verse. To put it simply, two words would have a low semantic distance (near zero) between them if they could be interchanged in a sentence without changing the overall meaning and context of said sentence (pairs like toad & frog, house & hut, or pencil & pen would be good examples). Our analysis found that if a lyricist is able to consistently provide pairs with low semantic distance, the song is far more well-liked.
                        </div>
                    </div>
                </div>
                
            </div>
            <div class="spacer"></div>
            <div class="footer">
                <p class="footer-text">Developed by Brayden Royston, Tailai Wang, and Bill Cui for Hack the North 2021.</p>
                <p class="footer-text">Works Cited: Coffee and Persistance.</p>
            </div>
        </div>
        <BarsBottom id="barBottom"/>
    </div>
</template>

<script>
import BarsBottom from '../Layout/BarsBottom.vue';

export default {
    components: {
        BarsBottom,
    }
}
</script>

<style scoped>
.how {
    height: 100vh;
    width: 100vw;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;

    position: relative;

    background: var(--black);
}

.root {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.title {
    width: 100%;
    font-family: var(--font-header);
    font-size: var(--fs-huge);
    color: white;
    margin: 0;
    text-align: center;
}

.body {
    display: flex;
    justify-content: space-around;
    align-items: flex-start;
}

a {
    color: white;
}

#subtitle {
    font-family: var(--font-header);
    font-size: var(--fs-medium);
    text-transform: capitalize;
    color: white;
    margin: 0;
    text-align: center;
}

.para-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;
}

.section {

    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

.para {
    color: white;
    font-size: var(--fs-extra-small);
    font-family: var(--font-body);
    padding: 10px;

}

.spacer {
    width: 100%;
    height: 5vh;
}


.footer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.footer-text {
    font-size: var(--fs-extra-small);
    color: white;
    font-family: var(--font-body);

}

#barBottom {
    position: absolute;
    left: 0;
    bottom: 0;
}
</style>