//
//  ResultsView.swift
//  lyricalculus
//
//  Created by Brayden Royston on 2021-09-18.
//

import SwiftUI

struct ResultsView: View {
    let lyrics: String
    
    var body: some View {
        ScrollView {
            Text("Overall Score: 9")
                .font(.title)
                .padding()
                .foregroundColor(Color.white)
                .background(Color.black)
                .clipShape(Capsule())
            VStack {
                HStack {
                    Text("Rhyme Score: 9")
                        .font(.body)
                        .padding()
                        .foregroundColor(Color.white)
                        .background(Color.blue)
                        .clipShape(Capsule())
                    
                    Text("Semantic Score: 10")
                        .font(.body)
                        .padding()
                        .foregroundColor(Color.white)
                        .background(Color.blue)
                        .clipShape(Capsule())
                }
                Text("Repetitiveness Score: 8")
                    .font(.body)
                    .padding()
                    .foregroundColor(Color.white)
                    .background(Color.blue)
                    .clipShape(Capsule())
            }
            Text("For repetition analysis, we generated TF-IDF Score for each line in a song before using a weighted average to give it a \"curated repetition score\". For example, aLip Pump's Gucci Gang would have a very high repetition score (which is bad).")
                .padding()
                .background(Color.black)
                .cornerRadius(20)
                .foregroundColor(Color.white)
                .padding()
            Spacer()
            Text("To assess semantic similarity, we used GloVe on different phrase endings in the song, which would give a semantic distance score that determines how the artist creatively connect parts of each verse. To put it simply, two words would have a low semantic distance (near zero) between them if they could be interchanged in a sentence without changing the overall meaning and context of said sentence (pairs like toad & frog, house & hut, or pencil & pen would be good examples). Our analysis found that if a lyricist is able to consistently provide pairs with low semantic distance, the song is far more well-liked.")
                .padding()
                .background(Color.black)
                .cornerRadius(20)
                .foregroundColor(Color.white)
                .padding()
                .cornerRadius(10)
        }
    }
}

struct ResultsView_Previews: PreviewProvider {
    static var previews: some View {
        ResultsView(lyrics: "hello")
    }
}
