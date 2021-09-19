//
//  CalculateView.swift
//  lyricalculus
//
//  Created by Brayden Royston on 2021-09-18.
//

import SwiftUI

struct CalculateView: View {
    @State var lyrics = ""
    
    var body: some View {
        Group {
            Text("Enter the lyrics below!")
                .padding()
                .font(.largeTitle)
            
            ZStack {
                TextEditor(text: $lyrics)
                Text(lyrics).opacity(0).padding(.all, 0.8)
            }
            .padding()
            .border(Color.black)
        }
        RobotLogo()
        NavigationLink(destination: ResultsView(lyrics: lyrics)) {
            Text("Calculate your favourite song!")
            .padding()
            .background(Color.black)
            .border(Color.black)
            .clipShape(Capsule())
            .font(.title)
            .foregroundColor(Color.white)
        }
    }
}

struct CalculateView_Previews: PreviewProvider {
    static var previews: some View {
        CalculateView()
    }
}
