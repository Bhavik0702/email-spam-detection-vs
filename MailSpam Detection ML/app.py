import pickle
import os
import sys

def load_model():
    model_path = "spam_model.pkl"
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            return pickle.load(f)
    else:
        print("Error: Model file 'spam_model.pkl' not found.")
        print("Please run train_model.py first to generate the model.")
        return None

def main():
    print("Loading model...")
    model = load_model()
    
    if not model:
        sys.exit(1)
        
    print("\n=== Spam Detection Terminal App ===")
    print("Type your message to check if it's Spam or Ham.")
    print("Type 'exit' or 'quit' to close the application.\n")
    
    while True:
        try:
            user_input = input("Enter message: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting application. Goodbye!")
                break
            
            if not user_input:
                continue
                
            # Predict
            prediction = model.predict([user_input])[0]
            
            # Get probabilities if possible
            try:
                proba = model.predict_proba([user_input])[0]
                confidence = max(proba) * 100
                confidence_str = f"({confidence:.2f}% confidence)"
            except AttributeError:
                confidence_str = ""
            
            print(f"Result: {prediction} {confidence_str}\n")
            
        except KeyboardInterrupt:
            print("\nExiting application. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
