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
        Text(lyrics)
    }
}

struct ResultsView_Previews: PreviewProvider {
    static var previews: some View {
        ResultsView(lyrics: "hello")
    }
}
