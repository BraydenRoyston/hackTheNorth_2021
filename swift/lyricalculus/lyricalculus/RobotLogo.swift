//
//  RobotLogo.swift
//  lyricalculus
//
//  Created by Brayden Royston on 2021-09-18.
//

import SwiftUI

struct RobotLogo: View {
    var body: some View {
        HStack {
            Image(systemName: "chevron.compact.right")
            Spacer()
                .frame(width: 30)
            Image(systemName: "chevron.compact.left")
        }
        VStack {
            HStack {
                Image(systemName: "smallcircle.circle")
                Image(systemName: "smallcircle.circle")
            }
            HStack {
                Image(systemName: "rectangle")
            }
        }
        .border(/*@START_MENU_TOKEN@*/Color.black/*@END_MENU_TOKEN@*/)
        .cornerRadius(10)
    }
}

struct RobotLogo_Previews: PreviewProvider {
    static var previews: some View {
        RobotLogo()
    }
}
