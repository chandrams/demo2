FROM openjdk:latest

WORKDIR /usr/src/myapp

COPY . .

# Compile the Java program
RUN javac Hello.java

# Run the Java program
CMD ["java", "Hello"]
