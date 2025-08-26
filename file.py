def file_read_write_challenge():
    """
    File Read & Write Challenge with Error Handling
    Reads a file, modifies the content, and writes to a new file
    """
    
    print("📁 File Read & Write Challenge 🖋️")
    print("=" * 50)
    
    # Get input filename from user
    while True:
        try:
            input_filename = input("Enter the input filename: ").strip()
            if not input_filename:
                print("❌ Filename cannot be empty. Please try again.")
                continue
                
            # Try to read the file
            with open(input_filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            print(f"✅ Successfully read: {input_filename}")
            break
            
        except FileNotFoundError:
            print(f"❌ Error: File '{input_filename}' not found. Please try again.")
        except PermissionError:
            print(f"❌ Error: Permission denied to read '{input_filename}'. Please try again.")
        except UnicodeDecodeError:
            print(f"❌ Error: Unable to decode file '{input_filename}'. It might be a binary file.")
        except IsADirectoryError:
            print(f"❌ Error: '{input_filename}' is a directory, not a file.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}. Please try again.")
    
    # Get output filename from user
    while True:
        try:
            output_filename = input("Enter the output filename: ").strip()
            if not output_filename:
                print("❌ Output filename cannot be empty. Please try again.")
                continue
            
            
            try:
                with open(output_filename, 'r'):
                    overwrite = input(f"⚠️  File '{output_filename}' already exists. Overwrite? (y/n): ").lower()
                    if overwrite != 'y':
                        print("Please enter a different output filename.")
                        continue
            except FileNotFoundError:
                pass  
            
            break
            
        except Exception as e:
            print(f"❌ Error: {e}. Please try again.")
    
    # Modify the content
    modified_content = modify_content(content)
    
    # Write to output file
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"✅ Successfully wrote modified content to: {output_filename}")
        print(f"📊 Original file size: {len(content)} characters")
        print(f"📊 Modified file size: {len(modified_content)} characters")
        
    except PermissionError:
        print(f"❌ Error: Permission denied to write to '{output_filename}'.")
    except Exception as e:
        print(f"❌ Unexpected error while writing: {e}")

def modify_content(content):
    """
    Modify the file content with various transformations
    """
    print("\n🔄 Modifying content...")
    

    modifications = [
        ("Original content", "No modifications"),
        ("Convert to uppercase", content.upper()),
        ("Convert to lowercase", content.lower()),
        ("Capitalize sentences", capitalize_sentences(content)),
        ("Add line numbers", add_line_numbers(content)),
        ("Remove extra spaces", remove_extra_spaces(content))
    ]
    
    # Show changes
    print("Choose a modification option:")
    for i, (desc, _) in enumerate(modifications):
        print(f"{i}. {desc}")
    
    # Get user
    while True:
        try:
            choice = int(input("Enter your choice (0-5): "))
            if 0 <= choice < len(modifications):
                selected_mod = modifications[choice][1]
                print(f"Selected: {modifications[choice][0]}")
                return selected_mod
            else:
                print("❌ Invalid choice. Please enter a number between 0-5.")
        except ValueError:
            print("❌ Please enter a valid number.")
        except Exception as e:
            print(f"❌ Error: {e}")

def capitalize_sentences(text):
    """Capitalize the first letter of each sentence"""
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return ' '.join(sentence.capitalize() for sentence in sentences)

def add_line_numbers(text):
    """Add line numbers to each line"""
    lines = text.split('\n')
    numbered_lines = [f"{i+1:3d}. {line}" for i, line in enumerate(lines)]
    return '\n'.join(numbered_lines)

def remove_extra_spaces(text):
    """Remove extra spaces from text"""
    import re

    text = re.sub(r' +', ' ', text)
    lines = text.split('\n')
    cleaned_lines = [line.strip() for line in lines]
    return '\n'.join(cleaned_lines)

def main():
    """Main function with error handling"""
    try:
        file_read_write_challenge()
        
        # Ask if user wants to continue
        while True:
            again = input("\n🔄 Would you like to process another file? (y/n): ").lower()
            if again == 'y':
                file_read_write_challenge()
            elif again == 'n':
                print("👋 Thank you for using the File Read & Write Challenge!")
                break
            else:
                print("❌ Please enter 'y' or 'n'.")
                
    except KeyboardInterrupt:
        print("\n\n⏹️  Program interrupted by user.")
    except Exception as e:
        print(f"💥 Critical error: {e}")
        print("Please restart the program.")


class FileProcessor:
    """Advanced file processing class with comprehensive error handling"""
    
    @staticmethod
    def safe_file_operation(filename, mode, operation):
        """Safely perform file operations with error handling"""
        try:
            with open(filename, mode, encoding='utf-8') as file:
                return operation(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found")
        except PermissionError:
            raise PermissionError(f"Permission denied for '{filename}'")
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"Unable to decode '{filename}'")
        except Exception as e:
            raise Exception(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Display welcome message
    print("🎯 File Read & Write Challenge with Error Handling 🧪")
    print("This program will:")
    print("1. 📖 Read a file with error handling")
    print("2. ✏️  Modify the content")
    print("3. 💾 Write to a new file")
    print("4. 🛡️  Handle various errors gracefully")
    print("-" * 60)
    
    main()