import { FlatList, SafeAreaView, StyleSheet, Text, View } from "react-native";

const DATA = [
  { id: "1", title: "Item da Lista 1", description: "Este é o primeiro item." },
  { id: "2", title: "Item da Lista 2", description: "Este é o segundo item." },
  { id: "3", title: "Item da Lista 3", description: "Este é o terceiro item." },
  { id: "4", title: "Item da Lista 4", description: "Este é o quarto item." },
  { id: "5", title: "Item da Lista 5", description: "Este é o quinto item." },
];

type ItemProps = { title: string; description: string };

const Item = ({ title, description }: ItemProps) => (
  <View style={styles.item}>
    <Text style={styles.itemTitle}>{title}</Text>
    <Text>{description}</Text>
  </View>
);

export default function ExploreScreen() {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>Tela de Exploração</Text>
      <FlatList
        data={DATA}
        renderItem={({ item }) => (
          <Item title={item.title} description={item.description} />
        )}
        keyExtractor={(item) => item.id}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 50,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 16,
    textAlign: "center",
  },
  item: {
    backgroundColor: "#f9f9f9",
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 16,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: "#eee",
  },
  itemTitle: {
    fontSize: 18,
    fontWeight: "bold",
  },
});
