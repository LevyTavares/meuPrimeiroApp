import { useState } from "react";
import { Pressable, StyleSheet, Text, View } from "react-native";

export default function ProfileScreen() {
  const [count, setCount] = useState(0);

  function handlePress() {
    setCount(count + 1);
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Minha Tela de Perfil</Text>
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
  },
  title: {
    textAlign: "center",
    fontSize: 30,
    fontWeight: "bold",
    marginBottom: 16,
    color: "blue",
  },
  counterText: {
    fontSize: 18,
    color: "blue",
  },
  button: {
    marginTop: 16,
    paddingVertical: 12,
    paddingHorizontal: 24,
    backgroundColor: "blue",
    borderRadius: 8,
  },
  buttonText: {
    color: "white",
    fontWeight: "bold",
  },
});
