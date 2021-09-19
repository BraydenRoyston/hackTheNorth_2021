//
//  ContentView.swift
//  lyricalculus
//
//  Created by Brayden Royston on 2021-09-18.
//

import SwiftUI

struct ContentView: View {
    @State private var willMove = false
    
    func pushCalculate() {
        willMove = true;
    }
    
    var body: some View {
        VStack {
            Text("Lyricalculus")
                .padding()
                .font(.largeTitle)
            Text("The music taste of a robot.")
                .padding()
                .font(.title3)
            VStack {
                RobotLogo()
                NavigationLink(destination: CalculateView()) {
                    Text("Calculate your favourite song!")
                    .padding()
                    .background(Color.black)
                    .border(Color.black)
                    .clipShape(Capsule())
                    .font(.title)
                    .foregroundColor(Color.white)
                }
                
//                Button(
//                    action: pushCalculate,
//                    label: {
//                        Text("Calculate your favourite song!")
//                        .padding()
//                        .background(Color.blue)
//                        .border(Color.black)
//                        .clipShape(Capsule())
//                        .font(.title)
//                        .foregroundColor(Color.white)
//                    }
//                )
                
            }
        }
        .navigate(to: CalculateView(), when: $willMove)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
