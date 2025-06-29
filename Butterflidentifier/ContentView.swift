//
//  ContentView.swift
//  Butterflidentifier
//
//  Created by David Tudor on 28/06/2025.
//

import SwiftUI
import SwiftData

struct ContentView: View {
    let butterflyIdModel = try? ButterflyClassifier(configuration: .init())
    @State var isPickerShowing = false
    @State var selectedImage: UIImage
    @State var modelOutput: String
    

    init() {
        selectedImage = UIImage(systemName: "person.circle.fill")! // THIS DEFAULT SHOULD BE CHANGED
        modelOutput = ""
        
    }
    
    var body: some View {
        VStack {
       
            Image(uiImage: selectedImage)
                .resizable()
                .aspectRatio(contentMode: .fill)
                .frame(width: 150, height: 150)
                .clipShape(Circle())
            
            Button {
                isPickerShowing = true
            } label: {
                Text("Change photo")
            }

            
            Text(modelOutput)
                .onChange(of: selectedImage) { oldImage, newImage in
                    do {
                        guard let image = newImage.cgImage else {
                            return
                        }
                        let input = try ButterflyClassifierInput(imageWith: image)
                        let output = try butterflyIdModel?.prediction(input: input)
                        
                        var outputString = ""
                        output?.targetProbability.enumerated().forEach({ key, value in
                            outputString += "\(key): \(value.value)\n"
                        })

                        modelOutput = outputString

                    } catch let error {
                        modelOutput = error.localizedDescription
                    }
                }
            
        }
        .sheet(isPresented: $isPickerShowing, onDismiss: nil) {
            ImagePicker(selectedImage: $selectedImage, isPickerShowing: $isPickerShowing)
        }
    }

}
