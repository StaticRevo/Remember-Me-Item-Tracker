import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function AddItemScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Add a New Item</Text>
      {/* You’ll add the form here later */}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
});
