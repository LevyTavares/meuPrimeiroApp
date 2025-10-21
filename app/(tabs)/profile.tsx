import { useState } from "react";
import { Pressable, StyleSheet, Text, View, TextInput } from "react-native";

export default function ProfileScreen() {
  const [count, setCount] = useState(0);

  const [name, setName] = useState('');

  function handlePress() {
    setCount(count + 1);
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Minha Tela de Perfil</Text>
      <Text style={styles.label}>Digite seu nome:</Text>
      <TextInput
        style={styles.input}
        placeholder="Seu nome aqui..."
        value={name}
        onChangeText={setName}
      />
      <Text style={styles.greeting}>Olá, {name || 'Visitante'}!</Text>
      <Text style={styles.counterText}>Você clicou: {count} vezes</Text>
      <Pressable style={styles.button} onPress={handlePress}>
        <Text style={styles.buttonText}>Clique Aqui</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#002a7f",
  },
  label: {
    fontSize: 18,
    color: "white",
    marginBottom: 8,
  },
  title: {
    textAlign: "center",
    fontSize: 30,
    fontWeight: "bold",
    marginBottom: 16,
    color: "orange",
  },
  input:{
    height: 40,
    width: '80%',
    borderColor: 'gray',
    borderWidth: 1,
    borderRadius: 8,
    paddingHorizontal: 10,
    marginTop: 8,
    marginBottom: 16,
  },
  greeting: {
    fontSize: 18,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 16,
  },
  counterText: {
    fontSize: 18,
    color: "orange",
  },
  button: {
    marginTop: 16,
    paddingVertical: 12,
    paddingHorizontal: 24,
    backgroundColor: "orange",
    borderRadius: 8,
  },
  buttonText: {
    color: "white",
    fontWeight: "bold",
  },
});
