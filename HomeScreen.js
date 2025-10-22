// HomeScreen.js
import { MaterialCommunityIcons } from "@expo/vector-icons";
import { LinearGradient } from "expo-linear-gradient";
import {
  Image,
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from "react-native";

const HomeScreen = ({ onNavigate }) => (
  <SafeAreaView style={styles.container}>
    <StatusBar barStyle="light-content" backgroundColor="#346a74" />

    <View style={styles.headerContainer}>
      <Image
        source={require("./assets/images/testify-icon.png")}
        style={styles.headerIcon}
      />
      <View style={styles.headerTextContainer}>
        <Text style={styles.headerTitle}>Testify</Text>
        <Text style={styles.headerSubtitle}>Seu assistente de avaliação</Text>
      </View>
    </View>

    <ScrollView contentContainerStyle={styles.scrollContent}>
      <Text style={styles.welcomeTitle}>Bem-vindo, Professor!</Text>

      <TouchableOpacity
        style={styles.heroButton}
        onPress={() => onNavigate("createTemplate")}
      >
        <LinearGradient colors={["#a1d5d1", "#5e9c98"]} style={styles.gradient}>
          <View style={styles.heroIconContainer}>
            <MaterialCommunityIcons
              name="file-document-plus-outline"
              size={32}
              color="#346a74"
            />
          </View>
          <View style={styles.heroTextContainer}>
            <Text style={styles.heroButtonText}>Criar um Novo Gabarito</Text>
            <Text style={styles.heroButtonSubtext}>
              Comece a criar sua próxima avaliação
            </Text>
          </View>
        </LinearGradient>
      </TouchableOpacity>

      <Text style={styles.sectionTitle}>Ações Rápidas</Text>

      <View style={styles.actionsGrid}>
        <TouchableOpacity
          style={styles.actionCard}
          onPress={() => onNavigate("corrector")}
        >
          <View style={styles.actionIconContainer}>
            <MaterialCommunityIcons
              name="camera-iris"
              size={28}
              color="#346a74"
            />
          </View>
          <Text style={styles.actionCardText}>Corrigir Provas</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.actionCard}
          onPress={() => onNavigate("reports")}
        >
          <View style={styles.actionIconContainer}>
            <MaterialCommunityIcons
              name="chart-bar"
              size={28}
              color="#346a74"
            />
          </View>
          <Text style={styles.actionCardText}>Ver Relatórios</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  </SafeAreaView>
);

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#f0f8f8" },
  scrollContent: { padding: 20 },
  headerContainer: {
    width: "100%",
    backgroundColor: "#346a74",
    paddingTop: Platform.OS === "android" ? 40 : 20,
    paddingBottom: 20,
    paddingHorizontal: 20,
    flexDirection: "row",
    alignItems: "center",
  },
  headerIcon: {
    width: 45,
    height: 45,
    borderRadius: 22.5,
    marginRight: 15,
  },
  headerTextContainer: {},
  headerTitle: { fontSize: 24, fontWeight: "bold", color: "#a1d5d1" },
  headerSubtitle: { fontSize: 14, color: "#f0f8f8" },
  welcomeTitle: {
    fontSize: 24,
    fontWeight: "600",
    color: "#333",
    marginBottom: 25,
  },
  heroButton: {
    width: "100%",
    borderRadius: 16,
    marginBottom: 30,
    elevation: 6,
    shadowColor: "#5e9c98",
    shadowOpacity: 0.4,
    shadowRadius: 8,
    shadowOffset: { width: 0, height: 4 },
  },
  gradient: {
    borderRadius: 16,
    padding: 20,
    flexDirection: "row",
    alignItems: "center",
  },
  heroIconContainer: {
    width: 60,
    height: 60,
    borderRadius: 30,
    backgroundColor: "rgba(255, 255, 255, 0.8)",
    justifyContent: "center",
    alignItems: "center",
    marginRight: 15,
  },
  heroTextContainer: {
    flex: 1,
  },
  heroButtonText: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#fff",
  },
  heroButtonSubtext: {
    fontSize: 14,
    color: "rgba(255, 255, 255, 0.9)",
    marginTop: 4,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: "600",
    color: "#555",
    marginBottom: 15,
  },
  actionsGrid: {
    flexDirection: "row",
    justifyContent: "space-between",
  },
  actionCard: {
    width: "48%",
    backgroundColor: "#fff",
    borderRadius: 12,
    paddingVertical: 25,
    paddingHorizontal: 15,
    alignItems: "center",
    elevation: 3,
    shadowColor: "#000",
    shadowOpacity: 0.08,
    shadowRadius: 8,
    borderWidth: 1,
    borderColor: "#E8F5F5",
  },
  actionIconContainer: {
    width: 60,
    height: 60,
    borderRadius: 30,
    backgroundColor: "#E8F5F5",
    justifyContent: "center",
    alignItems: "center",
    marginBottom: 15,
  },
  actionCardText: {
    fontSize: 15,
    fontWeight: "600",
    color: "#346a74",
    textAlign: "center",
  },
});

export default HomeScreen;
